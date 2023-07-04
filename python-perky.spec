Name:           python-perky
Version:        0.8.1
Release:        1%{?dist}
Summary:        A simple, Pythonic file format

License:        MIT
URL:            https://github.com/larryhastings/perky/
Source:         %{url}/archive/%{version}/perky-%{version}.tar.gz

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
* Thu Jun 29 2023 Maxwell G <maxwell@gtmx.me> - 0.8.1-1
- Initial package (rhbz#2218703).
