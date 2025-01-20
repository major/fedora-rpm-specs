%global srcname flake8-blind-except

Name:           python-%{srcname}
Version:        0.2.1
Release:        4%{?dist}
Summary:        A flake8 extension that checks for catch-all except statements

License:        MIT
URL:            https://github.com/elijahandrews/flake8-blind-except
Source0:        https://github.com/elijahandrews/flake8-blind-except/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
A flake8 extension that checks for blind, catch-all "except:" and
"except Exception:" statements.

As of pycodestyle 2.1.0, "E722 do not use bare except, specify exception
instead" is built-in. However, bare Exception and BaseException are still
allowed. This extension flags them as B902.

Using except without explicitly specifying which exceptions to catch is
generally considered bad practice, since it catches system signals like
SIGINT. You probably want to handle system interrupts differently than
exceptions occurring in your code.}

%description %_description


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  %{py3_dist pycodestyle}
BuildRequires:  %{py3_dist pytest}
Requires:       %{py3_dist flake8}
Requires:       %{py3_dist pycodestyle}

%description -n python%{python3_pkgversion}-%{srcname} %_description


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l flake8_blind_except


%check
%pytest --doctest-modules flake8_blind_except.py


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.rst


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Nov 21 2022 Scott K Logan <logans@cottsay.net> - 0.2.1-2
- Define _description variable to reduce duplication
- Drop macro from URL to improve ergonomics
- Enable doctest check using pytest

* Thu Nov 10 2022 Scott K Logan <logans@cottsay.net> - 0.2.1-1
- Initial package (rhbz#2141866)
