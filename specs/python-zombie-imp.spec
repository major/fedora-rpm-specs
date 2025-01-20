Name:           python-zombie-imp
Version:        0.0.2
Release:        8%{?dist}
Summary:        A copy of the `imp` module that was removed in Python 3.12

License:        Python-2.0.1
URL:            https://github.com/encukou/zombie-imp
Source:         %{pypi_source zombie-imp}

# Make the tests pass with Python 3.13.0a1+, 3.12.1+, 3.11.6+
Patch:          https://github.com/encukou/zombie-imp/commit/d45295faf4.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-test

%global _description %{expand:
A copy of the imp module that was removed in Python 3.12.
This is a compat package to ease transition to Python 3.12.
It shouldn't be used and packages using `imp` module
should use `importlib.metadata` instead.}

%description %_description

%package -n python3-zombie-imp
Summary:        %{summary}

# This package is deprecated, no new packages in Fedora can depend on it
Provides:       deprecated()

%description -n python3-zombie-imp %_description


%prep
%autosetup -p1 -n zombie-imp-%{version}


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files zombie_imp imp


%check
%tox


%files -n python3-zombie-imp -f %{pyproject_files}
%doc README.*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.0.2-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 24 2023 Miro Hrončok <mhroncok@redhat.com> - 0.0.2-3
- Make the tests pass with Python 3.13.0a1+, 3.12.1+, 3.11.6+

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 27 2023 Tomáš Hrnčiar <thrnciar@redhat.com> - 0.0.2-1
- Initial package

