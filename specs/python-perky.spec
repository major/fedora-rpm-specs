Name:           python-perky
Version:        0.9.3
Release:        2%{?dist}
Summary:        A simple, Pythonic file format

License:        MIT
URL:            https://github.com/larryhastings/perky/
Source:         %{url}/archive/%{version}/perky-%{version}.tar.gz
Patch:          use-flit_core-instead-of-flit-to-build-wheel.patch

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
A friendly, easy, Pythonic text file format.
Perky is a new, simple "rcfile" text file format for Python programs. It solves
the same problem as "INI" files, "TOML" files, and "JSON" files, but with its
own opinion about how to best solve the problem.}


%description %{_description}

%package -n     python3-perky
Summary:        %{summary}

%description -n python3-perky %{_description}


%prep
%autosetup -p1 -n perky-%{version}
# Remove shebang from non-executable file
sed -i -e '1{\@^#!.*@d}' perky/utility.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files perky


%check
cd tests
%{py3_test_envvars} %{python3} -m unittest discover


%files -n python3-perky -f %{pyproject_files}
# I don't like relying on %%pyproject_save_files for this
%license LICENSE
%doc README.md


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jan 13 2025 Maxwell G <maxwell@gtmx.me> - 0.9.3-1
- Update to 0.9.3. Fixes rhbz#2219611.

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.8.2-7
- Rebuilt for Python 3.13

* Mon Jan 29 2024 Maxwell G <maxwell@gtmx.me> - 0.8.2-6
- Use flit_core instead of flit to build wheel

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 0.8.2-2
- Rebuilt for Python 3.12

* Mon Jul 3 2023 Maxwell G <maxwell@gtmx.me> - 0.8.2-1
- Update to 0.8.2. Fixes rhbz#2219210.

* Thu Jun 29 2023 Maxwell G <maxwell@gtmx.me> - 0.8.1-1
- Initial package (rhbz#2218703).
