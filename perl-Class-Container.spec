#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Class-Container
Version  : 0.13
Release  : 7
URL      : https://cpan.metacpan.org/authors/id/K/KW/KWILLIAMS/Class-Container-0.13.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/K/KW/KWILLIAMS/Class-Container-0.13.tar.gz
Summary  : 'Glues object frameworks together transparently'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Class-Container-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Module::Implementation)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Params::Validate)
BuildRequires : perl(Try::Tiny)

%description
This archive contains the distribution Class-Container,
version 0.13:
Glues object frameworks together transparently

%package dev
Summary: dev components for the perl-Class-Container package.
Group: Development
Provides: perl-Class-Container-devel = %{version}-%{release}

%description dev
dev components for the perl-Class-Container package.


%package license
Summary: license components for the perl-Class-Container package.
Group: Default

%description license
license components for the perl-Class-Container package.


%prep
%setup -q -n Class-Container-0.13

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Class-Container
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Class-Container/LICENSE
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
/usr/lib/perl5/vendor_perl/5.28.1/Class/Container.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Class::Container.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Class-Container/LICENSE
