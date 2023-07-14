%bcond_without tests
%global debug_package   %{nil}

%global srcname pymatreader

%global desc %{expand:
A Python module to read Matlab files. This module works with both the old (<
7.3) and the new (>= 7.3) HDF5 based format. The output should be the same for
both kinds of files.

Documentation can be found here: http://pymatreader.readthedocs.io/en/latest/}

Name:           python-%{srcname}
Version:        0.0.30
Release:        4%{?dist}
Summary:        Convenient reader for Matlab mat files

License:        BSD
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://gitlab.com/obob/%{srcname}/-/archive/v%{version}/%{srcname}-v%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

# https://bugzilla.redhat.com/show_bug.cgi?id=2116690
ExcludeArch:    s390x

%description %{desc}

BuildRequires:  python3-devel

%package -n python3-%{srcname}

Summary:        %{summary}

BuildArch:      noarch

BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist future}
BuildRequires:  %{py3_dist h5py}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist scipy}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx_rtd_theme}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist twine}
BuildRequires:  %{py3_dist wheel}
BuildRequires:  %{py3_dist xmltodict}

%description -n python3-%{srcname} %{desc}

%package doc
Summary:        %{summary}

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{srcname}-v%{version}
rm -rf %{srcname}.egg-info

%generate_buildrequires
%pyproject_buildrequires -r

%build
%py3_build

pushd doc
    make SPHINXBUILD=sphinx-build-3 html
    rm -rf build/html/.doctrees
    rm -rf build/html/.buildinfo
    # conver to utf8
    pushd build/html
        iconv --from=ISO-8859-1 --to=UTF-8 objects.inv > objects.inv.new && \
        touch -r objects.inv objects.inv.new && \
        mv objects.inv.new objects.inv
    popd
popd

%install
%py3_install

%check
%if %{with tests}
# Reported upstream: https://gitlab.com/obob/pymatreader/-/issues/9
%{pytest} -k "not test_files_with_unsupported_classesv7"
%endif

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{srcname}

%files doc
%license LICENSE
%doc doc/build/html

%changelog
* Wed Jul 12 2023 Python Maint <python-maint@redhat.com> - 0.0.30-4
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 09 2022 Alessio <alciregi@fedoraproject.org> - 0.0.30-2
- Exclude s390x arch due to failing tests

* Sun Aug 07 2022 Alessio <alciregi@fedoraproject.org> - 0.0.30-1
- Update to 0.0.30
 
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.24-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 11 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 0.0.24-8
- Fix extra newline in description
- Drop unnecessary python_enable_dependency_generator macro

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.0.24-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.24-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 06 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.0.24-4
- Fix build

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.0.24-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 28 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.0.24-1
- Update to latest release

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.0.23-2
- Explicitly BR setuptools

* Sun Jun 21 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.0.23-1
- Update to 0.0.23

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.21-2
- Rebuilt for Python 3.9

* Sat Feb 01 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.0.21-1
- Update to latest release

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.19-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.19-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 08 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.0.19-1
- Update to latest upstream release 0.0.19

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 20 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.0.17-1
- Initial build
