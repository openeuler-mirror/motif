Name:          motif
Version:       2.3.4
Release:       19
Summary:       Run-time libraries and programs
License:       LGPLv2+
URL:           http://www.motifzone.net/
Source0:       http://downloads.sf.net/motif/motif-%{version}-src.tgz
Source1:       xmbind

BuildRequires: automake, libtool, autoconf, flex, flex-static, byacc, pkgconfig, libjpeg-devel libpng-devel
BuildRequires: libXft-devel libXmu-devel libXp-devel libXt-devel libXext-devel, xorg-x11-xbitmaps, perl-interpreter
Requires:      xorg-x11-xbitmaps, xorg-x11-xinit
Requires:      %{name}-help = %{version}-%{release} 
Provides:      openmotif = %{version}-%{release}
Obsoletes:     openmotif < %{version}
Conflicts:     lesstif <= 0.92.32-6

Patch0: motif-2.3.4-no_demos.patch
Patch1: openMotif-2.2.3-uil_lib.patch
Patch2: openMotif-2.3.0-rgbtxt.patch
Patch3: motif-2.3.4-mwmrc_dir.patch
Patch4: motif-2.3.4-bindings.patch
Patch5: openMotif-2.3.0-no_X11R6.patch
Patch6: motif-2.3.4-Fix-issues-with-Werror-format-security.patch

%description
This module is motif run-time environment, which includes the motif shared libraries.

%package devel
Summary:       Development files for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}, libjpeg-devel%{?_isa}, libpng-devel%{?_isa}, libXft-devel%{?_isa}
Requires:      libXmu-devel%{?_isa}, libXp-devel%{?_isa}, libXt-devel%{?_isa}, libXext-devel%{?_isa}
Provides:      openmotif-devel = %{version}-%{release}
Obsoletes:     openmotif-devel < 2.3.4
Provides:      %{name}-static%{?_isa} %{name}-static
Obsoletes:     %{name}-static
Conflicts:     lesstif-devel <= 0.92.32-6

%description devel
This package includes development files for %{name}.

%package        help
Summary:        man files for %{name}
Requires:       man

%description    help
This package includes man files for %{name}.

%prep
%autosetup -p1

%build
CFLAGS="$RPM_OPT_FLAGS -D_FILE_OFFSET_BITS=64"
./autogen.sh --libdir=%{_libdir} --enable-static --enable-xft --enable-jpeg --enable-png

%make_build clean
make -C include
%make_build

%install
%make_install
install -d $RPM_BUILD_ROOT/etc/X11/xinit/xinitrc.d
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/xinit/xinitrc.d/xmbind.sh

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_scriptlets

%files
%doc COPYING
/etc/X11/xinit/xinitrc.d/xmbind.sh
%dir /etc/X11/mwm
%config(noreplace) /etc/X11/mwm/system.mwmrc
%{_bindir}/mwm
%{_bindir}/xmbind
%{_includedir}/X11/bitmaps/*
%{_libdir}/*.so.*
%{_datadir}/X11/bindings

%files devel
%{_bindir}/uil
%{_includedir}/Mrm
%{_includedir}/Xm
%{_includedir}/uil
%{_libdir}/*.so
%{_libdir}/*.a

%files help
%{_mandir}/man*/*

%changelog
* Sat Nov 07 2020 Ge Wang <wangge20@huawei.com> - 2.3.4-19
- Set help package as montif package's install require

* Fri Nov 29 2019 openEuler Buildteam <buildteam@openeuler.org> - 2.3.4-18
- Package init
