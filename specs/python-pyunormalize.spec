%global pypi_name pyunormalize
%global git_commit 4b45c576567fb0293acb93a308c97cbaba3caa5f

Name:          python-%{pypi_name}
Version:       16.0.0
Release:       %autorelease
BuildArch:     noarch
Summary:       Unicode normalization forms (NFC, NFKC, NFD, NFKD)
# ./pyunormalize/_unicode.py is autogenerated from Unicode data and inherited
# its license (Unicode-3.0). The rest is licensed under MIT.
License:       MIT AND Unicode-3.0
URL:           https://github.com/mlodewijck/pyunormalize
VCS:           git:%{url}.git
Source0:       %{url}/archive/%{git_commit}/%{pypi_name}-%{git_commit}.tar.gz
BuildRequires: tox
BuildSystem:   pyproject
BuildOption(generate_buildrequires): -t
BuildOption(install): -l %{pypi_name}

%description
%{summary}.

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name}
%{summary}.

%check -a
%tox

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
