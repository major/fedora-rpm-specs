Name:           openkim-models
Version:        2021.01.28
%global         uversion %(v=%{version}; echo ${v//./-})
Release:        12%{?dist}
Summary:        Open Knowledgebase of Interatomic Models
# Automatically converted from old format: CDDL-1.0 and ASL 2.0 and MPLv2.0 and GPLv3 and LGPLv3 - review is highly recommended.
License:        CDDL-1.0 AND Apache-2.0 AND MPL-2.0 AND GPL-3.0-only AND LGPL-3.0-only
Url:            https://openkim.org
Source0:        https://s3.openkim.org/archives/collection/%{name}-%{uversion}.txz
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  cmake3 >= 3.10
BuildRequires:  kim-api-devel >= 2.2.1
BuildRequires:  vim

%description
OpenKIM is an online framework for making molecular simulations reliable,
reproducible, and portable.  Models conforming to the KIM application
programming interface work seamlessly with major simulation codes that have
adopted the KIM-API standard.

This package contains the models from openkim.org.

%prep
%setup -q -n %{name}-%{uversion}

%build
%{cmake3} -DCMAKE_SKIP_RPATH=ON -DKIM_API_MODEL_DRIVER_INSTALL_PREFIX=%{_libdir}/kim-api/model-drivers -DKIM_API_PORTABLE_MODEL_INSTALL_PREFIX=%{_libdir}/kim-api/portable-models -DKIM_API_SIMULATOR_MODEL_INSTALL_PREFIX=%{_libdir}/kim-api/simulator-models
%cmake_build

%install
%cmake_install
# Each model-driver and model is licensed separately.
# About 2/3 are CDDL-1.0, 1/4 public domain, and 1/12 GPL/LGPL
for i in $(find *model* -name "LICENSE*"); do echo ${i%/*}:; head -n 2 $i; echo;  done > LICENSE.models

%files
%license LICENSE LICENSE.models
%{_libdir}/kim-api/model-drivers/
%{_libdir}/kim-api/portable-models/
%{_libdir}/kim-api/simulator-models/

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2021.01.28-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 2021.01.28-11
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2021.01.28-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2021.01.28-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2021.01.28-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2021.01.28-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2021.01.28-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021.01.28-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021.01.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2021.01.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Feb 02 2021 Ryan S. Elliott <relliott@umn.edu> - 2021.01.28-2
- Adjust spec

* Mon Feb 01 2021 Ryan S. Elliott <relliott@umn.edu> - 2021.01.28-1
- Version bump to 2021.01.28

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2019.07.25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 04 2020 Christoph Junghans <junghans@votca.org> - 2019.07.25-4
- Fix out-of-source build on F33 (bug#1865159)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.07.25-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.07.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 12 2020 Ryan S. Elliott <relliott@umn.edu> - 2019.07.25-1
- Version bump to 2019.07.25

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.03.31-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019.03.31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 01 2019 Christoph Junghans <junghans@votca.org> - 2019.03.31-2
- Comments from review (bug #1703235)

* Wed Apr 24 2019 Christoph Junghans <junghans@votca.org> - 2019.03.31-1
- initial commit
