# Unset -s on python shebang - ensure that extensions installed with pip
# to user locations are seen and properly loaded
%global py3_shebang_flags %(echo %py3_shebang_flags | sed s/s//)

%global pypi_name nbclient

%global _description %{expand:
NBClient, a client library for programmatic notebook execution, is a tool for 
running Jupyter Notebooks in different execution contexts. NBClient was spun 
out of nbconvert (formerly ExecutePreprocessor). NBClient lets you execute notebooks.
}

Name:           python-%{pypi_name}
Version:        0.7.2
Release:        1%{?dist}
Summary:        A client library for executing notebooks

License:        BSD
URL:            https://jupyter.org
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel

%bcond_without check

%description
%_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%py_provides python3-%{pypi_name}

%description -n python3-%{pypi_name}
%_description

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires %{?with_check:-x test}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%if %{with check}
%check
%pytest -vv
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%{_bindir}/jupyter-execute


%changelog
* Wed Nov 30 2022 Lumír Balhar <lbalhar@redhat.com> - 0.7.2-1
- Update to 0.7.2 (rhbz#2132802)

* Mon Sep 12 2022 Lumír Balhar <lbalhar@redhat.com> - 0.6.8-1
- Update to 0.6.8
Resolves: rhbz#2125605

* Mon Aug 22 2022 Lumír Balhar <lbalhar@redhat.com> - 0.6.7-1
- Update to 0.6.7
Resolves: rhbz#2061198

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 0.5.11-4
- Rebuilt for Python 3.11

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.5.11-3
- Bootstrap for Python 3.11

* Fri Jun 10 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 0.5.11-2
- Backport PR#209 to drop (missing, implicit) dependency on ipython_genutils
Resolves: rbhz#2095849

* Tue Mar 01 2022 Lumír Balhar <lbalhar@redhat.com> - 0.5.11-1
- Update to 0.5.11 and fix tests with IPython 8.1
Resolves: rhbz#2054387

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 14 2022 Lumír Balhar <lbalhar@redhat.com> - 0.5.10-1
- Update to 0.5.10
Resolves: rhbz#2040501

* Tue Jan 04 2022 Lumír Balhar <lbalhar@redhat.com> - 0.5.9-1
- Update to 0.5.9
Resolves: rhbz#2022624

* Mon Nov 29 2021 Karolina Surma <ksurma@redhat.com> - 0.5.5-2
- Remove -s from Python shebang in `jupyter-execute` to let Jupyter see pip 
  installed extensions

* Tue Nov 09 2021 Lumír Balhar <lbalhar@redhat.com> - 0.5.5-1
- Update to 0.5.5
Resolves: rhbz#2021051

* Tue Aug 31 2021 Lumír Balhar <lbalhar@redhat.com> - 0.5.4-1
- Update to 0.5.4
Resolves: rhbz#1993880

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.5.3-3
- Rebuilt for Python 3.10

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.5.3-2
- Bootstrap for Python 3.10

* Sun Feb 28 2021 Lumír Balhar <lbalhar@redhat.com> - 0.5.3-1
- Update to 0.5.3

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan  7 17:08:21 CET 2021 Tomas Hrnciar <thrnciar@redhat.com> - 0.5.1-3
- Bootstrap for Python 3.10

* Sat Nov 28 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.5.1-2
- Change pytest invocation
- use py_provides macro

* Thu Nov 26 2020 Mukundan Ragavan <nonamedotc@gmail.com> - 0.5.1-1
- Initial package.
