#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v19
# autospec commit: f35655a
#
# Source0 file verified with key 0xD31B5563DAC1D4FA (adam@spiers.net)
#
Name     : stow
Version  : 2.4.1
Release  : 30
URL      : https://mirrors.kernel.org/gnu/stow/stow-2.4.1.tar.gz
Source0  : https://mirrors.kernel.org/gnu/stow/stow-2.4.1.tar.gz
Source1  : https://mirrors.kernel.org/gnu/stow/stow-2.4.1.tar.gz.sig
Source2  : D31B5563DAC1D4FA.pkey
Summary  : 'manage farms of symbolic links'
Group    : Development/Tools
License  : GPL-3.0
Requires: stow-bin = %{version}-%{release}
Requires: stow-info = %{version}-%{release}
Requires: stow-license = %{version}-%{release}
Requires: stow-man = %{version}-%{release}
Requires: stow-perl = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : gnupg
BuildRequires : perl(Test::Output)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Use-Perl-s-vendor-path.patch

%description
[![Build Status](https://travis-ci.org/aspiers/stow.svg)](https://travis-ci.org/aspiers/stow)
[![Coverage Status](https://coveralls.io/repos/aspiers/stow/badge.svg?branch=master&service=github)](https://coveralls.io/github/aspiers/stow?branch=master)

%package bin
Summary: bin components for the stow package.
Group: Binaries
Requires: stow-license = %{version}-%{release}

%description bin
bin components for the stow package.


%package doc
Summary: doc components for the stow package.
Group: Documentation
Requires: stow-man = %{version}-%{release}
Requires: stow-info = %{version}-%{release}

%description doc
doc components for the stow package.


%package info
Summary: info components for the stow package.
Group: Default

%description info
info components for the stow package.


%package license
Summary: license components for the stow package.
Group: Default

%description license
license components for the stow package.


%package man
Summary: man components for the stow package.
Group: Default

%description man
man components for the stow package.


%package perl
Summary: perl components for the stow package.
Group: Default
Requires: stow = %{version}-%{release}

%description perl
perl components for the stow package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) D31B5563DAC1D4FA' gpg.status
%setup -q -n stow-2.4.1
cd %{_builddir}/stow-2.4.1
%patch -P 1 -p1
pushd ..
cp -a stow-2.4.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1726067615
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1726067615
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/stow
cp %{_builddir}/stow-%{version}/COPYING %{buildroot}/usr/share/package-licenses/stow/31a3d460bb3c7d98845187c716a30db81c44b615 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/chkstow
/usr/bin/stow

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/stow/*

%files info
%defattr(0644,root,root,0755)
/usr/share/info/stow.info

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/stow/31a3d460bb3c7d98845187c716a30db81c44b615

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/stow.8

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
