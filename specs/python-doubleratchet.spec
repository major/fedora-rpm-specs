Name:           python-doubleratchet
Version:        1.3.0
Release:        1%{?dist}
Summary:        Python implementation of the Double Ratchet algorithm

License:        MIT
URL:            https://github.com/Syndace/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
# For tests
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
# For documentation
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3dist(sphinx-autodoc-typehints)
BuildRequires:  texinfo

%description
This python library offers an implementation of the Double Ratchet
algorithm.

A double ratchet allows message encryption providing perfect forward
secrecy. A double ratchet instance synchronizes with a second instance
using Diffie-Hellman calculations, that are provided by the DHRatchet
class.



%package     -n python3-doubleratchet
Summary:        Python implementation of the Double Ratchet algorithm

%description -n python3-doubleratchet
This python library offers an implementation of the Double Ratchet
algorithm.

A double ratchet allows message encryption providing perfect forward
secrecy. A double ratchet instance synchronizes with a second instance
using Diffie-Hellman calculations, that are provided by the DHRatchet
class.



%prep
%autosetup -n %{name}-%{version} -p1
# Do not measure coverage in tests
sed -i '/addopts = "--cov=doubleratchet --cov-report term-missing:skip-covered"/d' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
pushd docs
sphinx-build -b texinfo . texinfo
pushd texinfo
makeinfo --docbook doubleratchet.texi
popd
popd

%install
%pyproject_install
%pyproject_save_files doubleratchet
install -pDm0644 docs/texinfo/doubleratchet.xml \
  %{buildroot}%{_datadir}/help/en/python-doubleratchet/doubleratchet.xml

%check
%pyproject_check_import
%pytest tests 



%files -n python3-doubleratchet -f %{pyproject_files}
%license LICENSE
%doc README.md
%dir  %{_datadir}/help/en
%lang(en) %{_datadir}/help/en/python-doubleratchet


%changelog
* Mon Feb 02 2026 Benson Muite <fed500@fedoraproject.org> - 1.3.0-1
- Update to 1.3.0

* Mon Jan 26 2026 Benson Muite <fed500@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Sep 19 2025 Python Maint <python-maint@redhat.com> - 1.1.0-7
- Rebuilt for Python 3.14.0rc3 bytecode

* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 1.1.0-6
- Rebuilt for Python 3.14.0rc2 bytecode

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sun Jun 22 2025 Python Maint <python-maint@redhat.com> - 1.1.0-4
- Rebuilt for Python 3.14

* Sun Jun 08 2025 Benson Muite <fed500@fedoraproject.org> - 1.1.0-3
- Use newer packaging macros
- Build documentation

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jan 13 2025 Matthieu Saulnier <fantom@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0

* Wed Jul 24 2024 Matthieu Saulnier <fantom@fedoraproject.org> - 1.0.4-1
- Update to 1.0.4

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 29 2024 Python Maint <python-maint@redhat.com> - 1.0.3-3
- Rebuilt for Python 3.13

* Wed May 8 2024 Matthieu Saulnier <fantom@fedoraproject.org> - 1.0.3-2
- Remove useless variable in specfile (%%version_main)

* Wed May 1 2024 Matthieu Saulnier <fantom@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3
- Use %%pytest in %%check section instead of setup.py

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0~beta-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0~beta-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0~beta-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.7.0~beta-10
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0~beta-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0~beta-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.7.0~beta-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0~beta-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0~beta-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.7.0~beta-4
- Rebuilt for Python 3.10

* Sun Feb 14 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 0.7.0~beta-3
- Package Review RHBZ#1917089:
  - Fix the Version tag to match upstream version
  - Use %%{python3_version} in %%files section

* Mon Feb 08 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 0.7.0-2
- Remove upstream name variable used once: %%{srcname}
- Add more explicit description

* Sat Jan 16 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 0.7.0-1
- Initial package
