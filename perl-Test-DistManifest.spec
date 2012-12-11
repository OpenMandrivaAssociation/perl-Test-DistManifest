%define upstream_name    Test-DistManifest
%define upstream_version 1.011

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Verify MANIFEST as an author test
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Module::Manifest)
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(Test::Builder::Tester)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::NoWarnings)
BuildRequires:	perl(Module::Build)
BuildArch:	noarch

%description
This module provides a simple method of testing that a MANIFEST matches the
distribution.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
rm debugfiles.list debuglinks.list debugsources.list 
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sun May 15 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.11.0-1mdv2011.0
+ Revision: 674903
- new version

* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 1.9.0-2
+ Revision: 654308
- rebuild for updated spec-helper

* Sat Mar 27 2010 Jérôme Quelin <jquelin@mandriva.org> 1.9.0-1mdv2011.0
+ Revision: 528192
- import perl-Test-DistManifest


* Sat Mar 27 2010 cpan2dist 1.009-1mdv
- initial mdv release, generated with cpan2dist
