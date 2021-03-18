#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD31B5563DAC1D4FA (adam@spiers.net)
#
Name     : stow
Version  : 2.3.1
Release  : 18
URL      : https://mirrors.kernel.org/gnu/stow/stow-2.3.1.tar.gz
Source0  : https://mirrors.kernel.org/gnu/stow/stow-2.3.1.tar.gz
Source1  : https://mirrors.kernel.org/gnu/stow/stow-2.3.1.tar.gz.sig
Summary  : 'manage farms of symbolic links'
Group    : Development/Tools
License  : GPL-3.0
Requires: stow-bin = %{version}-%{release}
Requires: stow-info = %{version}-%{release}
Requires: stow-license = %{version}-%{release}
Requires: stow-man = %{version}-%{release}
Requires: stow-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Capture::Tiny)
BuildRequires : perl(IO::Scalar)
BuildRequires : perl(Test::Output)
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
%setup -q -n stow-2.3.1
cd %{_builddir}/stow-2.3.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1616077551
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1616077551
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/stow
cp %{_builddir}/stow-2.3.1/COPYING %{buildroot}/usr/share/package-licenses/stow/31a3d460bb3c7d98845187c716a30db81c44b615
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/chkstow
/usr/bin/stow

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/stow/*

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
/usr/lib/perl5/vendor_perl/5.32.1/Stow.pm
/usr/lib/perl5/vendor_perl/5.32.1/Stow/Util.pm
