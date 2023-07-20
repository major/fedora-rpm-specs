%bcond_without tests

%global forgeurl  https://github.com/CINPLA/exdir

Name:           python-exdir
Version:        0.4.2
Release:        %{autorelease}
Summary:        Directory structure standard for experimental pipelines
%forgemeta

License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}
# Use updated Versioneer
# AttributeError: module 'configparser' has no attribute 'SafeConfigParser'.
# SafeConfigParser was deprecated in Python 3.12
# https://github.com/CINPLA/exdir/pull/156
Patch0:         %{forgeurl}/pull/156.patch

BuildArch:      noarch

%global _description %{expand:
Experimental Directory Structure (exdir) is a proposed, open specification for
experimental pipelines. Exdir is currently a prototype published to invite
researchers to give feedback on the standard.

Exdir is an hierarchical format based on open standards. It is inspired by
already existing formats, such as HDF5 and NumPy, and attempts to solve some of
the problems assosciated with these while retaining their benefits. The
development of exdir owes a great deal to the efforts of others to standardize
data formats in science in general and neuroscience in particular, among them
the Klusta Kwik Team and Neurodata Without Borders.}

%description %_description

%package -n python3-exdir
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  git-core

# %%dir %%{_sysconfdir}/jupyter
# %%dir %%{_sysconfdir}/jupyter/jupyter_notebook_config.d
# %%dir %%{_sysconfdir}/jupyter/nbconfig
# %%dir %%{_sysconfdir}/jupyter/nbconfig/notebook.d
# %%dir %%{_datadir}/jupyter
# %%dir %%{_datadir}/jupyter/nbextensions
Requires:       python-jupyter-filesystem
# for the notebooks
Recommends:     %{py3_dist notebook}

%description -n python3-exdir %_description

%package doc
Summary:        Documentation for %{name}
BuildRequires:  make
BuildRequires:  %{py3_dist sphinx}
# The included copy is a fork and therefore can’t be unbundled. The
# original can be found at
# https://code.iamkate.com/javascript/collapsible-lists/ and was never
# versioned nor committed to version control.
Provides:       bundled(js-collapsible-lists)

%description doc
This package provides documentation for %{name}.

%prep
%autosetup -p1 -n exdir-%{version} -S git
# Remove 3rdparty directory
# Use git for removal, so Versioneer is not marking version as dirty
git rm -r 3rdparty

# Versioneer, you are a pain in the bottocks!
# Into submission wrangle you, I will!
python3 versioneer.py setup
git commit -m 'Did someone say versioneer? Into the void disappear!'
git tag -a -m '%{name}-%{version}-%{release}' %{version}


%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-r requirements.in}

%build
%pyproject_wheel

# Sometimes needed so sphinx can import the module
PYTHONPATH=".:.." make -C docs SPHINXOPTS=%{?_smp_mflags} html
rm -rf docs/_build/html/{.doctrees,.buildinfo} -vf

%install
%pyproject_install
%pyproject_save_files exdir

# Move jupyter bits to correct location
mkdir -p -m 0755 %{buildroot}%{_sysconfdir}
mv -v %{buildroot}%{_prefix}%{_sysconfdir}/jupyter %{buildroot}%{_sysconfdir}/jupyter

%check
%if %{with tests}
%{pytest}
%endif

%files -n python3-exdir -f %{pyproject_files}
%doc README.md
%{_datadir}/jupyter/nbextensions/exdir
%config(noreplace) %{_sysconfdir}/jupyter/jupyter_notebook_config.d/exdir.json
%config(noreplace) %{_sysconfdir}/jupyter/nbconfig/notebook.d/exdir.json

%files doc
%license LICENSE
%doc docs/_build/html examples

%changelog
%autochangelog
