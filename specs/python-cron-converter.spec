Name:           python-cron-converter
Version:        2.0.2
Release:        %autorelease
Summary:        Cron string parser and scheduler for Python

License:        MIT
URL:            https://github.com/Sonic0/cron-converter
Source:         %{url}/archive/v%{version}/cron-converter-%{version}.tar.gz

# Test test_timezone_offset_matches fails on Python 3.15.1+
# https://github.com/Sonic0/cron-converter/issues/46
Patch:          0001-Skip-test_timezone_offset_matches.patch

BuildSystem:    pyproject
BuildOption(install): --assert-license cron_converter

BuildArch:      noarch

%global common_description %{expand:
Cron-converter provides a Cron string parser (from string/lists to
string/lists) and iteration for the datetime object with a cron like format.}

%description %{common_description}


%package -n python3-cron-converter
Summary:        %{summary}

%description -n python3-cron-converter %{common_description}


%check -a
%{py3_test_envvars} %{python3} -m unittest discover --verbose tests/unit
%{py3_test_envvars} %{python3} -m unittest discover --verbose tests/integration


%files -n python3-cron-converter -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
