Name:		rakudo-Readline
Version:	0.1.5
Release:	8%{?dist}
Summary:	Simple Perl 6 binding to GNU libreadline

License:	Artistic 2.0
URL:		https://github.com/drforr/perl6-readline
Source0:	%url/archive/%{version}.tar.gz

BuildRequires:	rakudo >= %rakudo_rpm_version
Requires:	rakudo >= %rakudo_rpm_version
# readline is needed for the protected package: dnf
#BuildRequires:	readline
#Requires:	readline


%description
Perl 6 interface to GNU Readline, the CLI-based line reading library


%prep
%setup -q -n perl6-readline-%{version}


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
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 20 2019 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.1.5-1
- update to 0.1.5
- change the source to the new official tarfile

* Tue Sep 19 2017 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.2-0.1.20170918gita9f6dc4
- changed version and release tags

* Mon Sep 18 2017 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.20170918git.a9f6dc4-1
- create initail spec file
