# Polyfill %%bcond() macro for platforms without it
%if 0%{!?bcond:1}
%define bcond() %[ (%2)\
    ? "%{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}"\
    : "%{expand:%%{?_with_%{1}:%%global with_%{1} 1}}"\
]
%endif

# Set this to 1 when bootstrapping
%bcond bootstrap 0

%bcond tests 1
# Which packages to mask and which tests to do with native wrappers
%global wrapped_pkgs pygit2 rpm
%global wrappers_relevant_tests tests/rpmautospec/test_pkg_history.py tests/rpmautospec/subcommands/

# While bootstrapping, ignore manpages
%bcond manpages %{without bootstrap}

# The pytest-xdist package is not available when bootstrapping or on RHEL
%bcond xdist %[%{without bootstrap} && %{undefined rhel}]

# Package the placeholder rpm-macros (moved to redhat-rpm-config in F40)
%if ! (0%{?fedora} >= 40 || 0%{?rhel} >= 10)
%bcond rpmmacropkg 1
%else
%bcond rpmmacropkg 0
%endif

%if %{with bootstrap}
%bcond pyproject_macros 0
%else
%if ! 0%{?fedora}%{?rhel} || 0%{?fedora} || 0%{?epel} >= 9
%bcond pyproject_macros 1
# Appease old versions of hatchling
%if ! 0%{?fedora}%{?rhel} || 0%{?fedora} >= 41 || 0%{?rhel} >= 10
%bcond old_hatchling 0
%else
%bcond old_hatchling 1
%endif
%else
%bcond pyproject_macros 0
%endif
%endif

# Although this supports a range of libgit2 and librpm versions upstream,
# we want to ensure newer versions don’t accidentally break all packages using this.
# Hence we artificially restrict the Required version to what was tested during the build.
# When libgit2/librpm soname is bumped, this package needs to be rebuilt (and tested).
%define libgit2_lower_bound 1.7
%define libgit2_upper_bound 1.10
%define libgit2_requires %(rpm -q --provides libgit2 | grep '^libgit2\.so\.' | sed 's/()(64bit)$//' | head -n 1)

%global srcname rpmautospec

Name: python-%{srcname}
Version: 0.8.1

%if %{with bootstrap}
Release: 0%{?dist}
%else
Release: %autorelease
%endif
Summary: Package and CLI tool to generate release fields and changelogs
License: MIT AND GPL-2.0-only WITH GCC-exception-2.0 AND (MIT OR GPL-2.0-or-later WITH GCC-exception-2.0)
URL: https://github.com/fedora-infra/%{srcname}
Source0: %{pypi_source %{srcname}}
Source1: rpmautospec.in

%if 0%{!?pyproject_files:1}
%global pyproject_files %{_builddir}/%{name}-%{version}-%{release}.%{_arch}-pyproject-files
%endif

BuildArch: noarch
BuildRequires: findutils
BuildRequires: git
# the langpacks are needed for tests
BuildRequires: glibc-langpack-de
BuildRequires: glibc-langpack-en

BuildRequires: python3-devel >= 3.9.0
# Needed to build man pages
%if %{with manpages}
BuildRequires: python3dist(click-man)
%endif

%if %{with tests}
# The dependencies needed for testing don’t get auto-generated.
BuildRequires: python3dist(pytest)
%if %{with xdist}
BuildRequires: python3dist(pytest-xdist)
%endif
%endif

BuildRequires: python3dist(click)
BuildRequires: python3dist(click-plugins)
BuildRequires: python3dist(pygit2)
BuildRequires: python3dist(pyyaml)
BuildRequires: python3dist(rpm)
BuildRequires: sed

%if %{without pyproject_macros}
BuildRequires: python3dist(rpmautospec-core)
BuildRequires: python3dist(setuptools)
%{?python_provide:%python_provide python3-%{srcname}}
%endif

BuildRequires: (libgit2 >= %libgit2_lower_bound and libgit2 < %libgit2_upper_bound)
BuildRequires: rpm-libs
BuildRequires: rpm-build-libs

%global _description %{expand:
A package and CLI tool to generate RPM release fields and changelogs.}

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%package -n %{srcname}
Summary: CLI tool for generating RPM releases and changelogs

%if "%libgit2_requires" != ""
Requires: (%{libgit2_requires}()(64bit) or %{libgit2_requires})
Suggests: %{libgit2_requires}()(64bit)
%else
Requires: this-is-broken-libgit2-missing-during-build
%endif
Requires: rpm-libs
Requires: rpm-build-libs

Recommends: python3-%{srcname} = %{version}-%{release}
Recommends: python3-%{srcname}+click = %{version}-%{release}
Recommends: python3-%{srcname}+pygit2 = %{version}-%{release}
Recommends: python3-%{srcname}+rpm = %{version}-%{release}

%description -n %{srcname}
CLI tool for generating RPM releases and changelogs

%if %{with pyproject_macros}
%pyproject_extras_subpkg -n python3-%{srcname} click
%pyproject_extras_subpkg -n python3-%{srcname} pygit2
%pyproject_extras_subpkg -n python3-%{srcname} rpm
%pyproject_extras_subpkg -n python3-%{srcname} all
%else
%python_extras_subpkg -n python3-%{srcname} -i %{python3_sitelib}/*.dist-info click
%python_extras_subpkg -n python3-%{srcname} -i %{python3_sitelib}/*.dist-info pygit2
%python_extras_subpkg -n python3-%{srcname} -i %{python3_sitelib}/*.dist-info rpm
%python_extras_subpkg -n python3-%{srcname} -i %{python3_sitelib}/*.dist-info all
%endif

%if %{with rpmmacropkg}
%package -n rpmautospec-rpm-macros
Summary: Rpmautospec RPM macros for local rpmbuild
Requires: rpm

%description -n rpmautospec-rpm-macros
This package contains RPM macros with placeholders for building rpmautospec
enabled packages locally.
%endif

%generate_buildrequires
%if %{with pyproject_macros}
%pyproject_buildrequires
%endif

%prep
%autosetup -n %{srcname}-%{version}
%if %{without pyproject_macros}
sed -i -e 's/\[project\]/#\&/g' pyproject.toml
%else
%if %{with old_hatchling}
sed -i -e 's/license-files = \(\[.*\]\)/license-files = {globs = \1}/' pyproject.toml
%endif
%endif

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -i -e '/pytest-cov/d; /addopts.*--cov/d' pyproject.toml

%build
%if %{with pyproject_macros}
%pyproject_wheel
%else
%py3_build
%endif

%install
%if %{with pyproject_macros}
%pyproject_install
%pyproject_save_files %{srcname}
%else
%py3_install
cat << EOF > %{pyproject_files}
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/*.egg-info/
EOF
%endif

%if %{with manpages}
# Man pages
PYTHONPATH=%{buildroot}%{python3_sitelib} click-man rpmautospec
install -m755 -d %{buildroot}%{_mandir}/man1
install -m644 man/*.1 %{buildroot}%{_mandir}/man1
%endif

# RPM macros
%if %{with rpmmacropkg}
mkdir -p %{buildroot}%{rpmmacrodir}
install -m 644 rpm_macros.d/macros.rpmautospec %{buildroot}%{rpmmacrodir}/
%endif

# Shell completion
for shell_path in \
        bash:%{bash_completions_dir}/rpmautospec \
        fish:%{fish_completions_dir}/rpmautospec.fish \
        zsh:%{zsh_completions_dir}/_rpmautospec; do
    shell="${shell_path%%:*}"
    path="${shell_path#*:}"
    dir="${path%/*}"

    install -m 755 -d "%{buildroot}${dir}"

    PYTHONPATH=%{buildroot}%{python3_sitelib} \
    _RPMAUTOSPEC_COMPLETE="${shell}_source" \
    %{__python3} -c \
    "import sys; sys.argv[0] = 'rpmautospec'; from rpmautospec.cli import cli; sys.exit(cli())" \
    > "%{buildroot}${path}"
done

# Fill in the real version for the fallback method
touch -r %{buildroot}%{python3_sitelib}/rpmautospec/version.py timestamp
sed -i -e 's|0\.0\.0|%{version}|g' %{buildroot}%{python3_sitelib}/rpmautospec/version.py
touch -r timestamp %{buildroot}%{python3_sitelib}/rpmautospec/version.py

# Install bootstrapping copies of rpmautospec, rpmautospec_core packages
mkdir %{buildroot}%{_datadir}/rpmautospec-fallback
cp -r %{python3_sitelib}/rpmautospec_core %{buildroot}%{_datadir}/rpmautospec-fallback/
cp -r %{buildroot}%{python3_sitelib}/rpmautospec %{buildroot}%{_datadir}/rpmautospec-fallback/
find %{buildroot}%{_datadir}/rpmautospec-fallback \
    -depth -type d -a -name __pycache__ -exec rm -r {} \;

# Override the standard executable with a custom one that knows how to fall back
sed -e 's|@PYTHON3@|%{python3} -%{py3_shebang_flags}|g; s|@DATADIR@|%{_datadir}|g' \
    < %{S:1} \
    > %{buildroot}%{_bindir}/rpmautospec
chmod 755 %{buildroot}%{_bindir}/rpmautospec
touch -r %{S:1} %{buildroot}%{_bindir}/rpmautospec

%check
# Always run the import checks, even when other tests are disabled
%if %{with pyproject_macros}
%pyproject_check_import
%else
%py3_check_import rpmautospec rpmautospec.cli
%endif

%if %{with tests}
%pytest \
%if %{with xdist}
--numprocesses=auto
%endif

# And redo tests that are relevant for native bindings, but with the direct native wrappers.

# Poison the official package names…
for mod in %wrapped_pkgs; do
    echo "raise ImportError" > "${mod}.py"
done

%py3_test_envvars \
PYTHONPATH="$PWD:$PYTHONPATH" \
%__pytest \
%if %{with xdist}
--numprocesses=auto \
%endif
%wrappers_relevant_tests

# … and unpoison them again, just in case.
for mod in %wrapped_pkgs; do
    rm -f "${mod}.py"
done
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%files -n %{srcname}
%{_bindir}/rpmautospec
%{_datadir}/rpmautospec-fallback

%if %{with manpages}
%{_mandir}/man1/rpmautospec*.1*
%endif
%dir %{bash_completions_dir}
%{bash_completions_dir}/rpmautospec
%dir %{fish_completions_dir}
%{fish_completions_dir}/rpmautospec.fish
%dir %{zsh_completions_dir}
%{zsh_completions_dir}/_rpmautospec

%if %{with rpmmacropkg}
%files -n rpmautospec-rpm-macros
%{rpmmacrodir}/macros.rpmautospec
%endif

%changelog
%{?autochangelog}
