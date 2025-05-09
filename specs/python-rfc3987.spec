Name:           python-rfc3987
Version:        1.3.8
Release:        %autorelease
Summary:        Parsing and validation of URIs (RFC 3986) and IRIs (RFC 3987)

License:        GPL-3.0-or-later
URL:            https://codeberg.org/atufi/rfc3987
Source:         %{pypi_source rfc3987}

BuildSystem:            pyproject
BuildOption(install):   -l rfc3987

BuildArch:      noarch

%global _description %{expand:
This module provides regular expressions according to RFC 3986 “Uniform
Resource Identifier (URI): Generic Syntax”
<https://datatracker.ietf.org/doc/html/rfc3986> and RFC 3987 “Internationalized
Resource Identifiers (IRIs)” <https://datatracker.ietf.org/doc/html/rfc3987>,
and utilities for composition and relative resolution of references.}

%description %{_description}


%package -n     python3-rfc3987
Summary:        %{summary}

%description -n python3-rfc3987 %{_description}


%install -a
# Remove shebang from non-executable library file.
# https://codeberg.org/atufi/rfc3987/pulls/19
sed -r -i '1{/^#!/d}' %{buildroot}%{python3_sitelib}/rfc3987.py


%check -a
%{py3_test_envvars} %{python3} -m doctest -v rfc3987.py


%files -n python3-rfc3987 -f %{pyproject_files}
%doc README.txt


%changelog
%autochangelog
