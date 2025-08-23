%bcond_without tests

%global _description %{expand:
papermill is a tool for parameterizing, executing, and analyzing Jupyter
Notebooks.

Papermill lets you:

- parameterize notebooks
- execute notebooks

This opens up new opportunities for how notebooks can be used. For example:

- Perhaps you have a financial report that you wish to run with different
  values on the first or last day of a month or at the beginning or end of the
  year, using parameters makes this task easier.
- Do you want to run a notebook and depending on its results, choose a
  particular notebook to run next? You can now programmatically execute a
  workflow without having to copy and paste from notebook to notebook manually.

Papermill takes an opinionated approach to notebook parameterization and
execution based on our experiences using notebooks at scale in data pipelines.}


Name:           python-papermill
Version:        2.6.0
Release:        %{autorelease}
Summary:        Parameterize and run Jupyter and nteract Notebooks

License:        BSD-3-Clause
URL:            https://pypi.org/pypi/papermill
Source0:        %{pypi_source papermill}

# Drop the dependency on ansicolors
# https://github.com/nteract/papermill/pull/822
#
# Rebased on 2.6.0, without the diff for binder/requirements.txt since binder/
# is not included in the PyPI sdist.
Patch:          papermill-2.6.0-without-ansicolors.patch

BuildArch:      noarch
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%description %_description

%package -n python3-papermill
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  help2man

%if %{with tests}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-xdist}
BuildRequires:  %{py3_dist ipykernel}
BuildRequires:  %{py3_dist pyarrow}
%endif


%description -n python3-papermill %_description

%pyproject_extras_subpkg -n python3-papermill all s3 azure gcs hdfs github black

%prep
%autosetup -n papermill-%{version} -p1

sed -i 's/parametrize/parameterize/' setup.py

# Unpin aiohttp
sed -r -i 's/^(aiohttp).*$/\1/' requirements.txt

# Comment out to remove /usr/bin/env shebangs
# Can use something similar to correct/remove /usr/bin/python shebangs also
# find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'


%generate_buildrequires
%pyproject_buildrequires -x all


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l papermill


install -d '%{buildroot}%{_mandir}/man1'
help2man --no-info --version-string %{version} --help-option --help --no-discard-stderr --output='%{buildroot}%{_mandir}/man1/papermill.1' "%{buildroot}/%{_bindir}/papermill"

%check
%if %{with tests}
# require net access
%{pytest} -n auto -v\
    --ignore papermill/tests/test_abs.py \
    --ignore papermill/tests/test_adl.py \
    --ignore papermill/tests/test_s3.py \
    --ignore papermill/tests/test_autosave.py \
    -k "not GCSTest and not test_hdfs_listdir"
%endif

# LICENSE/COPYING are included in the dist-info, so we do not need to
# explicitly list them again
%files -n python3-papermill -f %{pyproject_files}
%doc README.md CHANGELOG.md
%{_bindir}/papermill
%{_mandir}/man1/papermill.*

%changelog
%autochangelog
