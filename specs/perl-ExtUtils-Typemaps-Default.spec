Name:           perl-ExtUtils-Typemaps-Default
Version:        1.07
Release:        %autorelease
Summary:        Set of useful typemaps
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/ExtUtils-Typemaps-Default
Source:         https://cpan.metacpan.org/authors/id/S/SM/SMUELLER/ExtUtils-Typemaps-Default-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::Typemaps) >= 3.18-292
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)

Requires:       perl(ExtUtils::Typemaps) >= 3.18-292

# Filtering unversioned requires
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(ExtUtils::Typemaps\\)$

%description
ExtUtils::Typemaps::Default is an ExtUtils::Typemaps subclass that provides
a set of default mappings (in addition to what perl itself provides). These
default mappings are currently defined as the combination of the mappings
provided by the following typemap classes which are provided in this
distribution:

ExtUtils::Typemaps::ObjectMap
ExtUtils::Typemaps::STL
ExtUtils::Typemaps::Basic

%prep
%autosetup -p1 -n ExtUtils-Typemaps-Default-%{version}

# this is fixed in BuildRequired version of ExtUtils::Typemap 3.18-292
sed -i 's/3.18_03/3.18/' Build.PL

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0

%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes
%dir %{perl_vendorlib}/ExtUtils/
%{perl_vendorlib}/ExtUtils/Typemap/
%{perl_vendorlib}/ExtUtils/Typemaps/
%{_mandir}/man3/ExtUtils::Typemap*

%changelog
%autochangelog
