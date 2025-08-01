%global pypi_name asn1tools

Name:          python-%{pypi_name}
Version:       0.167.0
Release:       %autorelease
BuildArch:     noarch
Summary:       ASN.1 parsing, encoding and decoding
License:       MIT
URL:           https://github.com/eerimoq/%{pypi_name}
VCS:           git:%{url}.git
Source0:       %{pypi_source %{pypi_name}}
BuildRequires: python3-diskcache
BuildRequires: python3-prompt-toolkit
BuildRequires: python3-pytest
BuildSystem:   pyproject
BuildOption(install): -l %{pypi_name}
# No python-bitstruct module available
ExcludeArch:   s390x

%description
%{summary}.

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name}
%{summary}.

%check -a
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%{_bindir}/asn1tools

%changelog
%autochangelog
