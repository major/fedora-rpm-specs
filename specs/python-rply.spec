Name:           python-rply
Version:        0.7.8
Release:        %autorelease
Summary:        Pure Python parser generator based on David Beazley’s PLY

License:        BSD-3-Clause
URL:            https://github.com/alex/rply
Source:         %{url}/archive/v%{version}/rply-%{version}.tar.gz

# Replace py with pytest
# https://github.com/alex/rply/pull/116
Patch:          %{url}/pull/116.patch

BuildSystem:    pyproject
BuildOption(install):   -l rply

BuildArch:      noarch

BuildRequires:  %{py3_dist pytest}

%global common_description %{expand:
Welcome to RPLY! A pure Python parser generator, that also works with RPython.
It is a more-or-less direct port of David Beazley's awesome PLY, with a new
public API, and RPython support.}

%description %{common_description}


%package -n python3-rply
Summary:        %{summary}

%description -n python3-rply %{common_description}


%check -a
%pytest -rs -v


%files -n python3-rply -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
