Name:           python-crochet
Version:        2.1.1
Release:        9%{?dist}
Summary:        A library that makes it easier to use Twisted from blocking code

# Patches needed for compatibility with Python 3.12
Patch1:         https://github.com/itamarst/crochet/pull/150.patch

License:        MIT
URL:            https://github.com/itamarst/crochet
Source0:        %{url}/archive/%{version}/crochet-%{version}.tar.gz
BuildArch:      noarch

%global _description %{expand:
Crochet is an MIT-licensed library that makes it easier to use Twisted from
regular blocking code. Some use cases include:

* Easily use Twisted from a blocking framework like Django or Flask.
* Write a library that provides a blocking API, but uses Twisted for its
  implementation.
* Port blocking code to Twisted more easily, by keeping a backwards
  compatibility layer.
* Allow normal Twisted programs that use threads to interact with Twisted more
  cleanly from their threaded parts. For example, this can be useful when using
  Twisted as a WSGI container.}


%description %_description


%package doc
Summary: Documentation for python-crochet

BuildRequires:  make
BuildRequires:  python3-sphinx

%description doc
Documentation for python-crochet.


%package -n python3-crochet
Summary:        %{summary}
BuildRequires:  python3-devel


%description -n python3-crochet %_description


%prep
%autosetup -p 1 -n crochet-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
%make_build -C docs html
rm docs/_build/html/.buildinfo


%install
%pyproject_install
%pyproject_save_files -l crochet


%check
%{py3_test_envvars} %{python3} -m unittest discover -v crochet.tests


%files -n python3-crochet -f %{pyproject_files}
%doc README.rst


%files doc
%license LICENSE
%doc docs/_build/html


%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 2.1.1-8
- Rebuilt for Python 3.14

* Mon Mar 31 2025 Carl George <carlwgeorge@fedoraproject.org> - 2.1.1-7
- Port to pyproject macros

* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 2.1.1-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Sep 15 2023 Jonathan Wright <jonathan@almalinux.org> - 2.1.1-1
- Update to 2.1.1

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 04 2023 Miro Hrončok <mhroncok@redhat.com> - 1.12.0-3
- Also require zombie-imp on runtime

* Wed Jun 28 2023 Python Maint <python-maint@redhat.com> - 1.12.0-2
- Rebuilt for Python 3.12

* Thu Mar 30 2023 Aurelien Bompard <abompard@fedoraproject.org> - 1.12.0-1
- Version 1.12.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 1.10.0-12
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.10.0-9
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 1.10.0-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.10.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 06 2019 Jeremy Cline <jcline@redhat.com> - 1.10.0-1
- Initial package.
