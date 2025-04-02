Name:           python-unix-ar
Version:        0.2.1
Release:        %autorelease
Summary:        .ar file handling for Python (including .deb)


License:        BSD-3-Clause
URL:            https://github.com/getninjas/unix_ar
Source:         %{url}/archive/%{version}/unix-ar-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
This packages allows the reading and writing of AR archive files.}

%description %{_description}

%package -n     python3-unix-ar
Summary:        %{summary}

%description -n python3-unix-ar %{_description}

%prep
%autosetup -n unix_ar-%{version}

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l unix_ar


%check
%{py3_test_envvars} %{python3} tests.py

%files -n python3-unix-ar -f %{pyproject_files}
%license LICENSE.txt
%doc README.md


%changelog
%autochangelog

