# Generated by go2rpm 1.10.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/cncf/udpa
%global goipath         github.com/cncf/udpa
Version:                0.0.1
%global commit          c52dc94e7fbe6449d8465faaeda22c76ca62d4ff

%gometa -L


%global common_description %{expand:
Universal Data Plane API Working Group (UDPA-WG).}

%global golicenses      LICENSE
%global godocs          DEVELOPER.md README.md

Name:           golang-github-cncf-udpa
Release:        15%{?dist}
Summary:        Universal Data Plane API Working Group (UDPA-WG)

License:        Apache-2.0
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

%generate_buildrequires
%go_generate_buildrequires

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Dec 07 2023 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 0.0.1-10
- Update to latest commit

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 10 2022 Maxwell G <gotmax@e.email> - 0.0.1-7
- Rebuild to fix FTBFS

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 23 13:28:44 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.1-1.20201223gitcc1b757
- Bump to commit cc1b757b3eddccaaaf0743cbb107742bb7e3ee4f

* Thu Sep 03 21:04:31 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.1-1
- Initial package
