%global srcname vcs2l

Name:           python-%{srcname}
Version:        1.1.6
Release:        %autorelease
Summary:        Command line tool designed to make working with multiple repositories easier

License:        Apache-2.0
URL:            https://github.com/ros-infrastructure/vcs2l/
Source0:        https://github.com/ros-infrastructure/vcs2l/archive/%{version}/%{srcname}-%{version}.tar.gz

# Merged upstream as ros-infrastructure/vcs2l#81, pending release
Patch0:         find_packages.patch
# Merged upstream as ros-infrastructure/vcs2l#82, pending release
Patch1:         temp_url.patch

BuildArch:      noarch

%global _description %{expand:
Vcs2l is a fork of Dirk Thomas's vcstool which is a version control system
(VCS) tool, designed to make working with multiple repositories easier.

This fork is created to continue the development of vcstool, as it is no
longer actively maintained.

The commands provided by vcs2l have the same naming structure as the original
fork, so it can be used as a drop-in replacement. Therefore, the repository is
renamed to vcs2l while maintaining the command names to vcstool to ensure
compatibility with existing scripts and workflows.}

%description %_description


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  git
BuildRequires:  mercurial
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  subversion
Conflicts:      python%{python3_pkgversion}-vcstool
Provides:       vcs2l = %{version}-%{release}
Recommends:     git

%description -n python%{python3_pkgversion}-%{srcname} %_description


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l vcs2l

# Move bash completion to the proper location
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
mv %{buildroot}%{_datadir}/vcs2l-completion/vcs.bash %{buildroot}%{bash_completions_dir}/vcs

# Move fish completion to the proper location
mkdir -p %{buildroot}%{_datadir}/fish/vendor_completions.d
mv %{buildroot}%{_datadir}/vcs2l-completion/vcs.fish %{buildroot}%{fish_completions_dir}/

# No global completion location for tcsh
rm %{buildroot}%{_datadir}/vcs2l-completion/vcs.tcsh

# Move zsh completion to the proper location
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions
mv %{buildroot}%{_datadir}/vcs2l-completion/vcs.zsh %{buildroot}%{zsh_completions_dir}/_vcs


%check
%pytest test


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc CHANGELOG.rst README.md SECURITY.md
%{_bindir}/vcs*
%{bash_completions_dir}/
%{fish_completions_dir}/
%{zsh_completions_dir}/


%changelog
%autochangelog
