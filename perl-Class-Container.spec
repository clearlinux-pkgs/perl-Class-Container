#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v13
# autospec commit: dc0ff31b4314
#
Name     : perl-Class-Container
Version  : 0.13
Release  : 34
URL      : https://cpan.metacpan.org/authors/id/K/KW/KWILLIAMS/Class-Container-0.13.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/K/KW/KWILLIAMS/Class-Container-0.13.tar.gz
Summary  : 'Glues object frameworks together transparently'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Class-Container-license = %{version}-%{release}
Requires: perl-Class-Container-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Module::Implementation)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Params::Validate)
BuildRequires : perl(Try::Tiny)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This archive contains the distribution Class-Container,
version 0.13:
Glues object frameworks together transparently

%package dev
Summary: dev components for the perl-Class-Container package.
Group: Development
Provides: perl-Class-Container-devel = %{version}-%{release}
Requires: perl-Class-Container = %{version}-%{release}

%description dev
dev components for the perl-Class-Container package.


%package license
Summary: license components for the perl-Class-Container package.
Group: Default

%description license
license components for the perl-Class-Container package.


%package perl
Summary: perl components for the perl-Class-Container package.
Group: Default
Requires: perl-Class-Container = %{version}-%{release}

%description perl
perl components for the perl-Class-Container package.


%prep
%setup -q -n Class-Container-0.13
cd %{_builddir}/Class-Container-0.13

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Class-Container
cp %{_builddir}/Class-Container-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Class-Container/87d1d7d8be19f13b0ee779177fa03fcca3e2b628 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Class::Container.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Class-Container/87d1d7d8be19f13b0ee779177fa03fcca3e2b628

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
