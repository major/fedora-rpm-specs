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

# The pytest-xdist package is not available when bootstrapping or on RHEL
%bcond xdist %[%{without bootstrap} && %{undefined rhel}]

# Whether to build only the minimal package for RHEL buildroot
%bcond minimal %[%{defined rhel} && %{undefined epel}]

# While bootstrapping or building the minimal package, ignore manpages
%bcond manpages %[%{without bootstrap} && %{without minimal}]

# While building the minimal package, ignore shell completions
%bcond completions %{without minimal}

# Package the placeholder rpm-macros (moved to redhat-rpm-config in F40)
%if ! (0%{?fedora} >= 40 || 0%{?rhel} >= 10)
%bcond rpmmacropkg 1
%else
%bcond rpmmacropkg 0
%endif

# Appease old versions of hatchling
%if ! 0%{?fedora}%{?rhel} || 0%{?fedora} >= 41 || 0%{?rhel} >= 10
%bcond old_hatchling 0
%else
%bcond old_hatchling 1
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
Version: 0.8.2

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
BuildRequires: python3dist(pyyaml)
%if %{with xdist}
BuildRequires: python3dist(pytest-xdist)
%endif
%endif

BuildRequires: sed

BuildRequires: (libgit2 >= %libgit2_lower_bound with libgit2 < %libgit2_upper_bound)
BuildRequires: rpm-libs
BuildRequires: rpm-build-libs

%global _description %{expand:
A package and CLI tool to generate RPM release fields and changelogs.}

%description %_description

%if %{without minimal}
%package -n python3-%{srcname}
Summary: %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%pyproject_extras_subpkg -n python3-%{srcname} click
%pyproject_extras_subpkg -n python3-%{srcname} pygit2
%pyproject_extras_subpkg -n python3-%{srcname} rpm
%pyproject_extras_subpkg -n python3-%{srcname} all
%endif

%package -n %{srcname}
Summary: CLI tool for generating RPM releases and changelogs

Provides: bundled(python3dist(rpmautospec)) = %{version}
Provides: bundled(python3dist(rpmautospec-core)) = %((rpm -q python3-rpmautospec-core --qf '%%{version}\n' || echo 0) | tail -n1)

%if "%libgit2_requires" != ""
Requires: (%{libgit2_requires}()(64bit) or %{libgit2_requires})
Suggests: %{libgit2_requires}()(64bit)
%else
Requires: this-is-broken-libgit2-missing-during-build
%endif
Requires: rpm-libs
Requires: rpm-build-libs

%if %{without minimal}
Recommends: python3-%{srcname} = %{version}-%{release}
Recommends: python3-%{srcname}+click = %{version}-%{release}
Recommends: python3-%{srcname}+pygit2 = %{version}-%{release}
Recommends: python3-%{srcname}+rpm = %{version}-%{release}
%endif

%description -n %{srcname}
CLI tool for generating RPM releases and changelogs

%if %{with rpmmacropkg}
%package -n rpmautospec-rpm-macros
Summary: Rpmautospec RPM macros for local rpmbuild
Requires: rpm

%description -n rpmautospec-rpm-macros
This package contains RPM macros with placeholders for building rpmautospec
enabled packages locally.
%endif

%generate_buildrequires
%pyproject_buildrequires %{!?with_minimal:-x all}

%prep
%autosetup -n %{srcname}-%{version}
%if %{with old_hatchling}
sed -i -e 's/license-files = \(\[.*\]\)/license-files = {globs = \1}/' pyproject.toml
%endif

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -i -e '/pytest-cov/d; /addopts.*--cov/d' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

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

%if %{with completions}
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
%endif

# Fill in the real version for the fallback method
touch -r %{buildroot}%{python3_sitelib}/rpmautospec/version.py timestamp
sed -i -e 's|0\.0\.0|%{version}|g' %{buildroot}%{python3_sitelib}/rpmautospec/version.py
touch -r timestamp %{buildroot}%{python3_sitelib}/rpmautospec/version.py

# Install bootstrapping copies of rpmautospec, rpmautospec_core packages
mkdir -p %{buildroot}%{_datadir}/rpmautospec-fallback
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
%pyproject_check_import %{?with_minimal:-e '*click*'}

%if %{with tests}
%if %{without minimal}
%pytest \
%if %{with xdist}
--numprocesses=auto
%endif
%endif

%if ! 0%{?rhel} || 0%{?rhel} >= 10
# And redo tests that are relevant for native bindings, but with the direct native wrappers, but not
# on EL <= 9 because the tests somehow run out of file descriptors.

# Poison the official package names…
mkdir -p poison-pill
for mod in %wrapped_pkgs; do
    echo "raise ImportError" > "poison-pill/${mod}.py"
    if PYTHONPATH="$PWD/poison-pill:$PYTHONPATH" %__python3 -c "import ${mod}" 2>/dev/null; then
        echo "Failed to poison-pill ${mod}!" >&2
        exit 1
    fi
done

%py3_test_envvars \
PYTHONPATH="$PWD/poison-pill:$PYTHONPATH" \
%__pytest \
%if %{with xdist}
--numprocesses=auto \
%endif
%wrappers_relevant_tests

%endif
%endif

%if %{without minimal}
%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%endif

%files -n %{srcname}
%{_bindir}/rpmautospec
%{_datadir}/rpmautospec-fallback

%if %{with manpages}
%{_mandir}/man1/rpmautospec*.1*
%endif
%if %{with completions}
%dir %{bash_completions_dir}
%{bash_completions_dir}/rpmautospec
%dir %{fish_completions_dir}
%{fish_completions_dir}/rpmautospec.fish
%dir %{zsh_completions_dir}
%{zsh_completions_dir}/_rpmautospec
%endif
%if %{with minimal}
%license licenses/*
%exclude %{python3_sitelib}
%endif

%if %{with rpmmacropkg}
%files -n rpmautospec-rpm-macros
%{rpmmacrodir}/macros.rpmautospec
%endif

%changelog
%{?autochangelog}
