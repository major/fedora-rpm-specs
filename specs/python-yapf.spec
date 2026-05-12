%global pypi_name yapf

%global desc %{expand: \
YAPF Introduction Most of the current formatters for Python e.g., autopep8, and
pep8ify are made to remove lint errors from code. This has some obvious
limitations. For instance, code that conforms to the PEP 8 guidelines may not
be}

%global forgeurl https://github.com/google/yapf

%global vimfiles_root %{_datadir}/vim/vimfiles

Name:           python-%{pypi_name}
Version:        0.43.0
Release:        %autorelease
Summary:        A formatter for Python code
# All code is under Apache-2.0 except bundled lib2to3  which is under PSF-2.0
License:        Apache-2.0 AND PSF-2.0

%global tag v%{version}
%forgemeta

URL:            %{forgeurl}
Source0:        %{forgesource}
Patch:          fix_installed_modules.patch
Patch:          fix_tox_requirements.patch

BuildArch:      noarch
 
BuildRequires:  python3-devel, git-core
BuildRequires:  python3dist(setuptools)
# Required for running tests
BuildRequires:  python3-importlib-metadata
BuildRequires:  python3-platformdirs

%description %{desc}

%package -n python3-%{pypi_name}
Summary:        %{summary}
Requires:       python3dist(setuptools)
# Upstream has forked lib2to3. From their README:
# A fork of python's lib2to3 with select features backported from black's
# blib2to3.
# Reasons for forking:
# - black's fork of lib2to3 already considers newer features like
#   Structured Pattern matching
# - lib2to3 itself is deprecated and no longer getting support
# Maintenance moving forward:
# - Most changes moving forward should only have to be done to the
#   grammar files in this project.
Provides:       bundled(python3dist(lib2to3))
%description -n python3-%{pypi_name} %{desc}

%package -n vim-%{pypi_name}
Summary:  %{summary}
Requires:      python3-%{pypi_name}
Requires:      vim-common

%description -n vim-%{pypi_name}
Enable formatting when using Vim.

%prep
%forgeautosetup -S git

# Remove shebang
sed -i '/^#!/d' third_party/yapf_third_party/_ylib2to3/pgen2/token.py


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{pypi_name} yapf_third_party

# Install vim plugins
install -Dm 0644 plugins/vim/autoload/yapf.vim \
  %{buildroot}%{vimfiles_root}/autoload/yapf.vim

install -Dm 0644 plugins/vim/plugin/yapf.vim \
  %{buildroot}%{vimfiles_root}/plugin/yapf.vim

%check
%tox


%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/yapf
%{_bindir}/yapf-diff

%files -n vim-%{pypi_name}
%doc plugins/README.md
%{vimfiles_root}/autoload/yapf.vim
%{vimfiles_root}/plugin/yapf.vim

%changelog
%autochangelog
