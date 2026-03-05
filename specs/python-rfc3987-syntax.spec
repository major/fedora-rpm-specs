Name:           python-rfc3987-syntax
Version:        1.1.0
Release:        %autorelease
Summary:        Helper functions to syntactically validate strings according to RFC 3987

License:        MIT
URL:            https://github.com/willynilly/rfc3987-syntax
Source:         %{url}/archive/v%{version}/rfc3987-syntax-%{version}.tar.gz

# Remove incorrect license data (trove classifier)
# https://github.com/willynilly/rfc3987-syntax/pull/13
Patch:          %{url}/pull/13.patch
# Fix a typo in RFC3987_SYNTAX_TERMS
# https://github.com/willynilly/rfc3987-syntax/pull/9
Patch:          %{url}/pull/9.patch

BuildSystem:            pyproject
BuildOption(install):   -l rfc3987_syntax
BuildOption(generate_buildrequires): -x testing

BuildArch:      noarch

%global _description %{expand:
Helper functions to parse and validate the syntax of terms defined in
RFC 3987 — the IETF standard for Internationalized Resource Identifiers (IRIs).

🎯 Purpose:

The goal of rfc3987-syntax is to provide a lightweight, permissively licensed
Python module for validating that strings conform to the ABNF grammar defined
in RFC 3987. These helpers are:

    ✅ Strictly aligned with the syntax rules of RFC 3987
    ✅ Built using a permissive MIT license
    ✅ Designed for both open source and proprietary use
    ✅ Powered by Lark, a fast, EBNF-based parser

🧠 Note: This project focuses on syntax validation only. RFC 3987 specifies
additional semantic rules (e.g., Unicode normalization, BiDi constraints,
percent-encoding requirements) that must be enforced separately.}

%description %{_description}


%package -n     python3-rfc3987-syntax
Summary:        %{summary}

%description -n python3-rfc3987-syntax %{_description}


%check -a
%pytest -v


%files -n python3-rfc3987-syntax -f %{pyproject_files}
%doc CITATION.cff
%doc README.md


%changelog
%autochangelog
