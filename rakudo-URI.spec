Name:		rakudo-URI
Version:	0.2.2
Release:	7%{?dist}
Summary:	Perl 6 realization of URI

License:	Artistic 2.0
URL:		https://github.com/perl6-community-modules/URI
Source0:	https://github.com/perl6-community-modules/uri/archive/v%{version}.tar.gz

BuildRequires:	rakudo >= %rakudo_rpm_version
Requires:	rakudo >= %rakudo_rpm_version


%description
Perl6 realization of URI - Uniform Resource Identifiers handler

A URI implementation using Perl 6 grammars to implement RFC 3986 BNF. Currently
only implements parsing. Includes URI::Escape to (un?)escape characters that
aren't otherwise allowed in a URI with % and a hex character numbering.


%prep
%setup -q -n uri-%{version}


%install
export QA_SKIP_BUILD_ROOT=1
RAKUDO_RERESOLVE_DEPENDENCIES=0 %perl6_mod_inst --to=%{buildroot}%{perl6_vendor_dir} --for=vendor


%check
perl6 -Ilib t/*.t


%files
%doc README.md
%license LICENSE
%{perl6_vendor_dir}/*/*


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jul 28 2019 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2.2-1
- Update to 0.2.2
- Add QA_SKIP_BUILD_ROOT=1
- Change to new source location

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-0.5.20170920gite5c8551
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-0.4.20170920gite5c8551
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 20 2017 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.1.4-0.1.20170920gite5c8551
- create initial spec file
