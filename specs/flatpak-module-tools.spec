%global srcname flatpak_module_tools
%global project_version 1.1.2

Name:		flatpak-module-tools
Version:	1.1.2
Release:	%autorelease
Summary:	Tools for maintaining Flatpak applications and runtimes as Fedora modules

License:	MIT
URL:		https://pagure.io/flatpak-module-tools
Source0:	https://releases.pagure.org/flatpak-module-tools/%{srcname}-%{project_version}.tar.gz

BuildArch:	noarch
# i386 is not supported by flatpak_module_tools.utils.Arch
ExcludeArch:	%{ix86}

BuildRequires: python3-devel

# For tests
BuildRequires: createrepo_c
BuildRequires: flatpak
BuildRequires: git-core
BuildRequires: libappstream-glib
BuildRequires: libmodulemd
BuildRequires: librsvg2
BuildRequires: ostree
# GI overrides for Modulemd
BuildRequires: python3-libmodulemd
# FIXME: python3-solv does not provide python3dist(solv)
BuildRequires: python3-solv
BuildRequires: zstd

Requires: python3-%{name}+cli = %{version}-%{release}
# FIXME: python3-solv does not provide python3dist(solv)
Requires: python3-solv

%description
flatpak-module-tools is a set of command line tools (all accessed via a single
'flatpak-module' executable) for operations related to maintaining Flatpak
applications and runtimes as Fedora modules.

%package -n python3-%{name}
Summary: Shared code for building Flatpak applications and runtimes from Fedora modules

# Note - pythonN-flatpak-modules-tools subpackage contains all the Python files from
# the upstream distribution, but some of them are only useful for the CLI, not
# for using this as a library for atomic-reactor. The dependencies here are those
# needed for library usage, the main package has the remainder.

Requires: createrepo_c
Requires: flatpak
# For appstream-compose
Requires: libappstream-glib
# for SVG gdk-pixbuf loader
Requires: librsvg2
Requires: ostree
Requires: zstd

# Output changed from <nvr>.oci.tar.gz to <nvr>.oci.tar
Conflicts: koji-flatpak <= 0.2

%description -n python3-%{name}
Python3 library for Flatpak handling


%pyproject_extras_subpkg -n python3-%{name} cli


%prep
%autosetup -p1 -n %{srcname}-%{project_version}
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -i -e '/pytest-cov/d' -e '/addopts/s/--cov[^ "]*//g' pyproject.toml
# FIXME: python3-solv does not provide python3dist(solv)
sed -i -e '/"solv"/d' pyproject.toml


%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{project_version}
%pyproject_buildrequires -x cli,tests


%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{project_version}
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l flatpak_module_tools


%check
%pyproject_check_import
# Tests using RPM don't work well inside %%check
%pytest -k "not test_create_rpm_manifest"


%files
%license LICENSE
%doc README.md
%{_bindir}/flatpak-module
%{_bindir}/flatpak-module-depchase


%files -n python3-%{name} -f %{pyproject_files}


%changelog
%autochangelog
