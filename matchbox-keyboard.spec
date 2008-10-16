#specfile originally created for Fedora, modified for Moblin Linux

%define libfakekey_version 0.1

Name:           matchbox-keyboard
Version:        0.1
Release:        %mkrel 2.5
Summary:        On screen virtual keyboard

Group:          Accessibility
License:        GPLv2+
URL:            http://matchbox-project.org/
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Patch0:         matchbox-keyboard-0.1-fix-desktop.patch

BuildRequires:  %{mklibname -d fakekey} >= %{libfakekey_version}
BuildRequires:  libpng-devel
BuildRequires:  libxft-devel
BuildRequires:  libxtst-devel
BuildRequires:  expat-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libxi-devel

%description
Matchbox-keyboard is an on screen 'virtual' or 'software'
keyboard. It will hopefully work well on various touchscreen
devices from mobile phones to tablet PCs running X Windows.

It aims to 'just work' supporting localised, easy to write
XML layout configuration files.


%prep
%setup -q
%patch0 -p1 -b .fix-category

%build
%configure --disable-applet
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

desktop-file-install --vendor="" --delete-original \
  --dir=$RPM_BUILD_ROOT%{_datadir}/applications \
  $RPM_BUILD_ROOT%{_datadir}/applications/inputmethods/*.desktop


%post
update-desktop-database &> /dev/null ||:


%postun
update-desktop-database &> /dev/null ||:


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_bindir}/matchbox-keyboard
%{_datadir}/matchbox-keyboard/
%{_datadir}/pixmaps/*
%{_datadir}/applications/*

