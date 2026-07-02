%bcond_without check

Name:           python-humanize
Version:        4.16.0
Release:        %autorelease
Summary:        Turns dates in to human readable format, e.g '3 minutes ago'

License:        MIT
URL:            https://github.com/python-humanize/humanize
Source0:        %{pypi_source humanize}

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
This modest package contains various common humanization utilities, like turning
a number into a fuzzy human readable duration ('3 minutes ago') or into a human
readable size or throughput.}

%description %_description


%package -n python3-humanize
Summary: %summary


%description -n python3-humanize %_description


%prep
%autosetup -n humanize-%{version}

# Remove shebangs from libs.
for lib in src/humanize/filesize.py; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new && mv $lib.new $lib
done

# Remove .po files
find -name '*.po' -delete

%pyproject_patch_dependency pytest-codspeed:ignore
%pyproject_patch_dependency pytest-cov:ignore
# Don't run coverage report during %%check
sed -i '/core:coverage.exceptions.CoverageWarning/d' pyproject.toml
sed -Ei 's/ ?--cov(-[^ ]+)? +[^ ]+//g' tox.ini


%generate_buildrequires
%pyproject_buildrequires %{?with_check:-t}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l humanize


%if %{with check}
%check
%tox
%endif


%files -n python3-humanize -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
