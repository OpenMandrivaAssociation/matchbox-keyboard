%define date	20150602

%define	major	0
%define	libname	%mklibname matchbox-keyboard %{major}
%define	devname	%mklibname -d matchbox-keyboard

Name:           matchbox-keyboard
Version:        0.1
Release:        1
Summary:        On screen virtual keyboard

Group:          Accessibility
License:        GPLv2+
URL:            http://matchbox-project.org/
Source0:	%{name}-%{version}-%{date}.tar.xz
Patch0:         matchbox-keyboard-0.1-fix-desktop.patch

BuildRequires:	pkgconfig(libfakekey)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(expat)
BuildRequires:  desktop-file-utils
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(matchbox-panel)

%description
Matchbox-keyboard is an on screen 'virtual' or 'software'
keyboard. It will hopefully work well on various touchscreen
devices from mobile phones to tablet PCs running X Windows.

It aims to 'just work' supporting localised, easy to write
XML layout configuration files.

%package -n	%{libname}
Group:		System/Libraries
Summary:	On screen virtual keyboard

%description -n	%{libname}
Libraries for the Matchbox Desktop.

%package -n	%{devname}
Group:		Development/C
Summary:	Static libraries and header files from %{name}
Provides:	matchbox-keyboard-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n	%{devname}
Static libraries and header files for %{name}.


%prep
%setup -qn %{name}-%{version}-%{date}
%apply_patches
# for newer libtool
autoreconf -fiv

%build
export LDFLAGS=-lX11
%configure --enable-gtk-im --enable-applet
%make


%install
%makeinstall_std

desktop-file-install --vendor="" --delete-original \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/inputmethods/*.desktop
rmdir %{buildroot}%{_datadir}/applications/inputmethods

%files
%doc AUTHORS COPYING README
%{_bindir}/matchbox-keyboard
%{_datadir}/matchbox-keyboard/
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%{_libdir}/matchbox-panel/libkeyboard.so
%{_libdir}/gtk-2.0/2.10.0/immodules/libmb-im-invoker.so

%files -n %{libname}
%{_libdir}/libmatchbox-keyboard.so.%{major}*

%files -n %{devname}
%{_libdir}/libmatchbox-keyboard.so
%{_libdir}/pkgconfig/libmatchbox-keyboard.pc
%{_includedir}/libmatchbox-keyboard/*.h
