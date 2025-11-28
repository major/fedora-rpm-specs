Name:           python-cron-converter
Version:        1.3.0
Release:        %autorelease
Summary:        Cron string parser and scheduler for Python

License:        MIT
URL:            https://github.com/Sonic0/cron-converter
Source:         %{url}/archive/v%{version}/cron-converter-%{version}.tar.gz

# fix: test_timezone should not compare utcoffset across DST boundaries #33
# https://github.com/Sonic0/cron-converter/pull/33
#
# Fixes:
#
# test_timezone started failing when Europe/Rome entered DST
# https://github.com/Sonic0/cron-converter/issues/32
#
# Rebased on v1.3.0.
Patch:          0001-fix-test_timezone-should-not-compare-utcoffset-acros.patch

BuildSystem:            pyproject
BuildOption(install):   -l cron_converter

BuildArch:      noarch

%global common_description %{expand:
Cron-converter provides a Cron string parser (from string/lists to
string/lists) and iteration for the datetime object with a cron like format.}

%description %{common_description}


%package -n python3-cron-converter
Summary:        %{summary}

%description -n python3-cron-converter %{common_description}


%check -a
%{py3_test_envvars} %{python3} -m unittest discover -v tests/unit
%{py3_test_envvars} %{python3} -m unittest discover -v tests/integration


%files -n python3-cron-converter -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
