Name:           kim-api
Version:        2.2.1
%global sover   2
Release:        11%{?dist}
Summary:        Open Knowledgebase of Interatomic Models KIM API
License:        CDDL-1.0
Url:            https://www.openkim.org
Source0:        https://s3.openkim.org/kim-api/kim-api-%{version}.txz
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  pkgconfig
BuildRequires:  bash-completion
%global b_compdir %(pkg-config --variable=completionsdir bash-completion)
%if "%{b_compdir}" == ""
%global b_compdir /etc/bash_completion.d
%endif
%global z_compdir %{_datadir}/zsh/site-functions
BuildRequires:  cmake3 >= 3.4
BuildRequires:  vim

%description
OpenKIM is an online framework for making molecular simulations reliable,
reproducible, and portable.  Models conforming to the KIM application
programming interface work seamlessly with major simulation codes that have
adopted the KIM-API standard.

This package can be used to load all the files (libraries, headers, and
documentation) for the KIM-API.

%package devel
Summary:    Development headers and libraries for kim-api
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
OpenKIM is an online framework for making molecular simulations reliable,
reproducible, and portable.  Models conforming to the KIM application
programming interface work seamlessly with major simulation codes that have
adopted the KIM-API standard.

This package contains the development files (headers and documentation) for the
KIM-API.

%package examples
Summary:    Example models for kim-api
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description examples
OpenKIM is an online framework for making molecular simulations reliable,
reproducible, and portable.  Models conforming to the KIM application
programming interface work seamlessly with major simulation codes that have
adopted the KIM-API standard.

This package contains the example models for the KIM-API.

%prep
%setup -q

%build
%{cmake3} -DCMAKE_SKIP_RPATH=ON -DCMAKE_INSTALL_LIBEXECDIR=%{_libexecdir} -DBASH_COMPLETION_COMPLETIONSDIR=%{b_compdir} -DZSH_COMPLETION_COMPLETIONSDIR=%{z_compdir}
%cmake_build

%install
%cmake_install

# emacs files
mkdir -p %{buildroot}%{_datadir}/emacs/site-lisp
mv %{buildroot}/usr/share/emacs/site-lisp/kim-api/kim-api-c-style.el %{buildroot}%{_datadir}/emacs/site-lisp/kim-api-c-style.el
rm %{buildroot}/usr/share/doc/kim-api/{LICENSE.CDDL,NEWS}

%ldconfig_scriptlets

%files
%doc README.md NEWS
%license LICENSE.CDDL
%{_bindir}/kim-api-*
%dir %{_libexecdir}/kim-api
%{_libexecdir}/kim-api/kim-api-*
%{_libdir}/libkim-api.so.%{sover}*
%{b_compdir}/kim-api-collections-management.bash
%{z_compdir}/_kim-api-collections-management
%{_datadir}/emacs/site-lisp/kim-api-c-style.el

%files devel
%{_includedir}/kim-api/
%{_libdir}/kim-api/mod/
%{_datadir}/cmake/
%dir %{_libdir}/kim-api/
%{_libdir}/libkim-api.so
%{_libdir}/pkgconfig/libkim-api.pc

%files examples
%{_libdir}/kim-api/model-drivers/
%{_libdir}/kim-api/portable-models/
%{_libdir}/kim-api/simulator-models/

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 14 14:51:28 MST 2020 Christoph Junghans <junghans@votca.org> - 2.2.1-1
- Version bump to v2.2.1 (bug #1907279)

* Wed Nov 18 19:45:40 MST 2020 Christoph Junghans <junghans@votca.org> - 2.2.0-1
- Version bump to v2.2.0 (bug #1899347)

* Mon Aug 03 2020 Christoph Junghans <junghans@votca.org> - 2.1.3-5
- Fix out-of-source build on F33 (bug #1863940)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 26 2019 Christoph Junghans <junghans@votca.org> - 2.1.3-1
- Version bump to 2.1.3 (bug #1742785)

* Tue Jul 30 2019 Ryan S. Elliott <relliott@umn.edu> - 2.1.2-1
- update to 2.1.2 and add zsh completions

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 06 2019 Christoph Junghans <junghans@votca.org> - 2.0.2-3
- fix pkg-config file on 32-bit archs

* Sat Apr 13 2019 Christoph Junghans <junghans@votca.org> - 2.0.2-2
- Comments from review (bug #1699487)

* Wed Apr 10 2019 Christoph Junghans <junghans@votca.org> - 2.0.2-1
- Initial commit
