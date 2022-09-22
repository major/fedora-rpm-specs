%undefine __cmake_in_source_build
%global _vpath_srcdir src

Name:           daggy
Version:        2.1.3
Release:        1%{?dist}
Summary:        Data Aggregation Utility and developer library

License:        MIT
URL:            https://github.com/synacker/daggy
Source0:        %{url}/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  qt6-qtbase-devel
BuildRequires:  gcc-c++
BuildRequires:  mustache-devel
BuildRequires:  libssh2-devel
BuildRequires:  yaml-cpp-devel
BuildRequires:  cmake
ExcludeArch: s390x


%description
Data Aggregation Utility and C/C++ developer library for data streams catching.
Main goals are server-less, cross-platform, simplicity and ease-of-use.
It can be helpful for developers, QA, DevOps and engineers for debug, 
analyze and control any data streams, including requests and responses, 
in distributed network systems, for example, based on micro-service architecture.

%package devel
Summary: Development files for %{name}

%description devel
%{summary}

%prep
%autosetup

%build
%cmake -DVERSION=%{version} src
%cmake_build

%install
%cmake_install

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}:${LD_LIBRARY_PATH}
%ctest

%files
%license LICENSE
%doc docs/*.md
%{_bindir}/%{name}
%{_libdir}/libDaggyCore.so

%post
daggy --version

%files devel
%{_includedir}/DaggyCore

%changelog
* Sun Aug 28 2022 Mikhail Milovidov <milovidovmikhail@gmail.com> - 2.1.3-1
- Updated daggy version up to 2.1.3

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 16 2022 Mikhail Milovidov <milovidovmikhail@gmail.com> - 2.1.2-1
- Update up to 2.1.2

* Fri Jan 07 2022 Mikhail Milovidov <milovidovmikhail@gmail.com> - 2.1.1-3
- Added ctest execution

* Mon Jan 03 2022 Mikhail Milovidov <milovidovmikhail@gmail.com> - 2.1.1-2
- Exclude s390x

* Mon Jan 03 2022 Mikhail Milovidov <milovidovmikhail@gmail.com> - 2.1.1-1
- Updated daggy version up to 2.1.1

* Mon Jan 03 2022 Mikhail Milovidov <milovidovmikhail@gmail.com> - 2.1.0-1
- Updated daggy version

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 20 2020 Mikhail Milovidov <milovidovmikhail@gmail.com> - 2.0.2-1
- Update up to 2.0.2 version

* Tue Apr 07 2020 Mikhail Milovidov <milovidovmikhail@gmail.com> - 2.0.1-1
- Update up to 2.0.1 version. Fix typos in description

* Sun Apr 05 2020 Mikhail Milovidov <milovidovmikhail@gmail.com>
- Update to 2.0.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 26 2020 Benjamin Kircher <bkircher@0xadd.de> - 1.1.3-3
- Rebuild for botan2-2.13

* Fri Oct 18 2019 Richard Shaw <hobbes1069@gmail.com> - 1.1.3-2
- Rebuild for yaml-cpp 0.6.3.

* Thu Jul 25 2019 Mikhail Milovidov <milovidovmikhail@gmail.com> - 1.1.3-1
- Update to 1.2.3

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 23 2019 Mikhail Milovidov <milovidovmikhail@gmail.com> - 1.1.2-1
- Update to 1.1.2

* Fri Jun 21 2019 Mikhail Milovidov <milovidovmikhail@gmail.com> - 1.1.1-1
- Update to 1.1.1

* Sun Jun 16 20:04:20 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0

* Tue Mar 19 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1

* Sat Mar 16 2019 Mikhail Milovidov <milovidovmikhail@gmail.com> - 1.0.0-1
- Initial rpm release
