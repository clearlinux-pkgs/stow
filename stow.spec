#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD31B5563DAC1D4FA (adam@spiers.net)
#
Name     : stow
Version  : 2.2.2
Release  : 3
URL      : http://ftp.gnu.org/gnu/stow/stow-2.2.2.tar.gz
Source0  : http://ftp.gnu.org/gnu/stow/stow-2.2.2.tar.gz
Source99 : http://ftp.gnu.org/gnu/stow/stow-2.2.2.tar.gz.sig
Summary  : 'manage the installation of multiple software packages'
Group    : Development/Tools
License  : GPL-2.0
Requires: stow-bin
Requires: stow-doc
BuildRequires : perl(Capture::Tiny)
BuildRequires : perl(IO::Scalar)
BuildRequires : perl(Test::Output)

%description
===================
This is GNU Stow, a symlink farm manager program which takes distinct
packages of software and/or data located in separate directories on
the filesystem, and makes them appear to be installed in the same
place.  For example, /usr/local/bin could contain symlinks to files
within /usr/local/stow/emacs/bin, /usr/local/stow/perl/bin etc., and
likewise recursively for any other subdirectories such as .../share,
.../man, and so on.

%package bin
Summary: bin components for the stow package.
Group: Binaries

%description bin
bin components for the stow package.


%package doc
Summary: doc components for the stow package.
Group: Documentation

%description doc
doc components for the stow package.


%prep
%setup -q -n stow-2.2.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1506189059
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1506189059
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/Stow.pm
/usr/lib/perl5/site_perl/5.26.1/Stow/Util.pm

%files bin
%defattr(-,root,root,-)
/usr/bin/chkstow
/usr/bin/stow

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/stow/*
%doc /usr/share/info/*
%doc /usr/share/man/man8/*
