%bcond_without tests

Name:           conda
Version:        4.14.0
Release:        %autorelease
Summary:        Cross-platform, Python-agnostic binary package manager

License:        BSD and ASL 2.0 and LGPLv2+ and MIT
# The conda code is BSD
# progressbar is LGPLv2+
# six is MIT/X11
# adapters/ftp.py is ASL 2.0

URL:            http://conda.pydata.org/docs/
Source0:        https://github.com/conda/conda/archive/%{version}/%{name}-%{version}.tar.gz
# bash completion script moved to a separate project
Source1:        https://raw.githubusercontent.com/tartansandal/conda-bash-completion/1.5/conda
Patch0:         conda_sys_prefix.patch
Patch1:         conda_gateways_disk_create.patch
# Do not test with conda-build
Patch2:         conda-conda-build.patch
# Use system cpuinfo
Patch3:         conda-cpuinfo.patch
# Fix tests on 32bit
# https://github.com/conda/conda/pull/9759
Patch4:         conda-32bit.patch
# Fix mock import
Patch5:         conda-mock.patch
# Use new (0.15) ruamel-yaml API
Patch6:         https://patch-diff.githubusercontent.com/raw/conda/conda/pull/11632.patch

Patch10001:     0001-Fix-toolz-imports.patch
Patch10004:     0004-Do-not-try-to-run-usr-bin-python.patch
Patch10005:     0005-Fix-failing-tests-in-test_api.py.patch
Patch10006:     0006-shell-assume-shell-plugins-are-in-etc.patch
Patch10007:     0001-Add-back-conda-and-conda_env-entry-point.patch
Patch10008:     0002-Go-back-to-ruamel_yaml.patch

BuildArch:      noarch

BuildRequires:  pkgconfig(bash-completion)
%global bash_completionsdir %(pkg-config --variable=completionsdir bash-completion 2>/dev/null || echo '/etc/bash_completion.d')
BuildRequires:  sed

Requires:       python%{python3_pkgversion}-conda = %{version}-%{release}
# Removed upstream in favour of calling "conda activate" in version 4.4.0
Obsoletes:      conda-activate < 4.4

%?python_enable_dependency_generator


%global _description %{expand:
Conda is a cross-platform, Python-agnostic binary package manager. It
is the package manager used by Anaconda installations, but it may be
used for other systems as well. Conda makes environments first-class
citizens, making it easy to create independent environments even for
C libraries. Conda is written entirely in Python.

The Fedora conda base environment is special.  Unlike a standard
anaconda install base environment it is essentially read-only.  You
can only use conda to create and manage new environments.}


%description %_description

%global _py3_reqs \
        python%{python3_pkgversion}-cpuinfo \
        python%{python3_pkgversion}-conda-package-handling >= 1.3.0 \
        python%{python3_pkgversion}-distro >= 1.0.4 \
        python%{python3_pkgversion}-frozendict >= 1.2 \
        python%{python3_pkgversion}-pycosat >= 0.6.3 \
        python%{python3_pkgversion}-pyOpenSSL >= 16.2.0 \
        python%{python3_pkgversion}-pyyaml \
        python%{python3_pkgversion}-requests >= 2.18.4 \
        python%{python3_pkgversion}-ruamel-yaml >= 0.11.14 \
        python%{python3_pkgversion}-tqdm >= 4.22.0 \
        python%{python3_pkgversion}-urllib3 >= 1.19.1
%global py3_reqs %(c="%_py3_reqs"; echo "$c" | xargs)


%package -n python%{python3_pkgversion}-conda
Summary:        %{summary}

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  %py3_reqs
# When this is present, vendored toolz should not be used
%if 0%{?fedora} || 0%{?rhel} >= 8
# EPEL7 does not have new enough cytoolz
BuildRequires:  python%{python3_pkgversion}-cytoolz >= 0.8.2
%endif
# For tests
BuildRequires:  python-unversioned-command
BuildRequires:  python%{python3_pkgversion}-boto3
BuildRequires:  python%{python3_pkgversion}-pytest-rerunfailures
BuildRequires:  python%{python3_pkgversion}-pytest-timeout
BuildRequires:  python%{python3_pkgversion}-pytest-xprocess
BuildRequires:  python%{python3_pkgversion}-responses

Requires:       %py3_reqs
%if 0%{?fedora} || 0%{?rhel} >= 8
# EPEL does not have new enough cytoolz
Requires:       python%{python3_pkgversion}-cytoolz >= 0.8.2
%endif
Provides:       bundled(python%{python3_pkgversion}-appdirs) = 1.2.0
Provides:       bundled(python%{python3_pkgversion}-auxlib)
Provides:       bundled(python%{python3_pkgversion}-boltons) = 18.0.0
Provides:       bundled(python%{python3_pkgversion}-six) = 1.10.0
Provides:       bundled(python%{python3_pkgversion}-toolz) = 0.8.2

%{?python_provide:%python_provide python%{python3_pkgversion}-conda}

%description -n python%{python3_pkgversion}-conda %_description

%prep
%autosetup -p1

sed -r -i 's/^(__version__ = ).*/\1"%{version}"/' conda/__init__.py
# xdoctest not packaged
sed -i -e '/xdoctest/d' setup.cfg

# delete interpreter line, the user can always call the file
# explicitly as python3 /usr/lib/python3.6/site-packages/conda/_vendor/appdirs.py
# or so.
sed -r -i '1 {/#![/]usr[/]bin[/]env/d}' conda/_vendor/appdirs.py

# Use Fedora's cpuinfo since it supports more arches
rm -r conda/_vendor/cpuinfo

# Replaced by cytools, byte compilation fails under python3.7
%if 0%{?fedora} || 0%{?rhel} >= 8
# EPEL does not have new enough cytoolz
# We need to keep __init__.py which does the dispatch between vendored and non-vendored
rm conda/_vendor/toolz/[a-zA-Z]*
%endif

# Use system versions
# TODO - urllib3 - results in test failures: https://github.com/conda/conda/issues/9512
#rm -r conda/_vendor/{distro.py,frozendict.py,tqdm,urllib3}
#find conda -name \*.py | xargs sed -i -e 's/^\( *\)from .*_vendor\.\(\(distro\|frozendict\|tqdm\|urllib3\).*\) import/\1from \2 import/'
rm -r conda/_vendor/{distro.py,frozendict,tqdm}
find conda -name \*.py | xargs sed -i -e 's/^\( *\)from .*_vendor\.\(\(distro\|frozendict\|tqdm\).*\) import/\1from \2 import/'

%ifnarch x86_64
# Tests on 32-bit
cp -a tests/data/conda_format_repo/linux-{64,32}
sed -i -e s/linux-64/linux-32/ tests/data/conda_format_repo/linux-32/*json
# Tests on non-x86_64
cp -a tests/data/conda_format_repo/{linux-64,%{python3_platform}}
sed -i -e s/linux-64/%{python3_platform}/ tests/data/conda_format_repo/%{python3_platform}/*json
%endif

# do not run coverage in pytest
sed -i -E '/--(no-)?cov/d' setup.cfg


%build
# build conda executable
%py3_build

%install
# install conda executable
%py3_install

mkdir -p %{buildroot}%{_sysconfdir}/conda/condarc.d
mkdir -p %{buildroot}%{_datadir}/conda/condarc.d
cat >%{buildroot}%{_datadir}/conda/condarc.d/defaults.yaml <<EOF
pkgs_dirs:
 - /var/cache/conda/pkgs
 - ~/.conda/pkgs
EOF

mkdir -p %{buildroot}%{_localstatedir}/cache/conda/pkgs/cache

# install does not create the directory on EL7
install -m 0644 -Dt %{buildroot}/etc/profile.d/ conda/shell/etc/profile.d/conda.{sh,csh}
sed -r -i '1i CONDA_EXE=%{_bindir}/conda' %{buildroot}/etc/profile.d/conda.sh
sed -r -i -e '1i set _CONDA_EXE=%{_bindir}/conda\nset _CONDA_ROOT=' \
          -e 's/CONDA_PFX=.*/CONDA_PFX=/' %{buildroot}/etc/profile.d/conda.csh
install -m 0644 -Dt %{buildroot}/etc/fish/conf.d/ conda/shell/etc/fish/conf.d/conda.fish
sed -r -i -e '1i set -gx CONDA_EXE "/usr/bin/conda"\nset _CONDA_ROOT "/usr"\nset _CONDA_EXE "/usr/bin/conda"\nset -gx CONDA_PYTHON_EXE "/usr/bin/python3"' \
          %{buildroot}/etc/fish/conf.d/conda.fish

# Install bash completion script
install -m 0644 -Dt %{buildroot}%{bash_completionsdir}/ %SOURCE1


%check
%if %{with tests}
export PATH=%{buildroot}%{_bindir}:$PATH
PYTHONPATH=%{buildroot}%{python3_sitelib} conda info

# Integration tests generally require network, so skip them.

# TestJson.test_list does not recognize /usr as a conda environment
# These fail on koji with PackageNotFound errors likely due to network issues
# test_cli.py::TestRun.test_run_returns_int
# test_cli.py::TestRun.test_run_returns_nonzero_errorlevel
# test_cli.py::TestRun.test_run_returns_zero_errorlevel

# test_ProgressiveFetchExtract_prefers_conda_v2_format, test_subdir_data_prefers_conda_to_tar_bz2,
# test_use_only_tar_bz2 fail in F31 koji, but not with mock --enablerepo=local. Let's disable
# them for now.
# tests/cli/test_main_{clean,rename}.py tests require network access
# tests/core/test_initialize.py tries to unlink /usr/bin/python3 and fails when python is a release candidate
# tests/core/test_solve.py::test_cuda_fail_1 fails on non-x86_64
py.test-%{python3_version} -vv -m "not integration" \
    --ignore conda/auxlib/_vendor \
    --deselect=tests/test_cli.py::TestJson::test_list \
    --deselect=tests/test_cli.py::test_run_returns_int \
    --deselect=tests/test_cli.py::test_run_returns_nonzero_errorlevel \
    --deselect=tests/test_cli.py::test_run_returns_zero_errorlevel \
    --deselect=tests/test_cli.py::test_run_readonly_env \
    --deselect=tests/cli/test_main_clean.py \
    --deselect=tests/cli/test_main_rename.py \
    --deselect=tests/core/test_package_cache_data.py::test_ProgressiveFetchExtract_prefers_conda_v2_format \
    --deselect=tests/core/test_subdir_data.py::test_subdir_data_prefers_conda_to_tar_bz2 \
    --deselect=tests/core/test_subdir_data.py::test_use_only_tar_bz2 \
    --deselect=tests/core/test_initialize.py \
    --deselect=tests/core/test_solve.py::test_cuda_fail_1
%endif

%files
%{_sysconfdir}/conda/
%{_bindir}/conda
%{_bindir}/conda-env
%{bash_completionsdir}/conda
# TODO - better ownership/requires for fish
%dir /etc/fish
%dir /etc/fish/conf.d
/etc/fish/conf.d/conda.fish
/etc/profile.d/conda.sh
/etc/profile.d/conda.csh

%files -n python%{python3_pkgversion}-conda
%license LICENSE.txt
%doc CHANGELOG.md README.md
%{python3_sitelib}/conda/
%{python3_sitelib}/conda_env/
%{python3_sitelib}/*.egg-info
%{_localstatedir}/cache/conda/
%{_datadir}/conda/


%changelog
%autochangelog
