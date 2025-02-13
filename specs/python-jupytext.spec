# NOTE: sphinx-gallery support requires a version <= 0.8.  Upstream will
# accept patches to make it work with later versions.

%global giturl  https://github.com/mwouts/jupytext
#global vsuffix d

Name:           python-jupytext
Version:        1.16.7
Release:        %autorelease
Summary:        Save Jupyter notebooks as text documents or scripts

License:        MIT
BuildArch:      noarch
URL:            https://jupytext.readthedocs.io/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/jupytext-%{version}%{?vsuffix}.tar.gz
# Source1 and Source2 created with ./prepare_vendor.sh
Source1:        jupytext-%{version}-vendor.tar.xz
Source2:        jupytext-%{version}-vendor-licenses.txt
Source3:        prepare_vendor.sh

# s390x builds fail due to a bug in jupyterlab
# https://bugzilla.redhat.com/show_bug.cgi?id=2278011
ExcludeArch:    s390x

BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  nodejs-devel
BuildRequires:  nodejs-npm
BuildRequires:  pandoc
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}

# Temporary workaround for https://bugzilla.redhat.com/show_bug.cgi?id=2275382
BuildRequires:  nodejs-full-i18n

%global _desc %{expand:
Have you always wished Jupyter notebooks were plain text documents?
Wished you could edit them in your favorite IDE?  And get clear and
meaningful diffs when doing version control?  Then... Jupytext may well
be the tool you're looking for!

Jupytext is a plugin for Jupyter that can save Jupyter notebooks as
- Markdown files (or MyST Markdown files, or R Markdown or Quarto text
  notebooks)
- Scripts in many languages.

Common use cases for Jupytext are:
- Doing version control on Jupyter Notebooks
- Editing, merging or refactoring notebooks in your favorite text editor
- Applying Q&A checks on notebooks.}

%description %_desc

%package -n python3-jupytext
Summary:        %{summary}
# Filesystem package for the standard Jupyter paths
Requires:       python-jupyter-filesystem

%description -n python3-jupytext %_desc

%package -n python3-jupyterlab-jupytext
# The jupytext project is released under the MIT license.  Bundled JavaScript:
# base64-js: MIT
# buffer: MIT
# ieee754: BSD-3-Clause
# jupyterlab-rise: BSD-3-Clause
License:        MIT AND BSD-3-Clause
Summary:        Jupyterlab extension to invoke jupytext
Requires:       python3-jupytext = %{version}-%{release}
Requires:       jupyterlab >= 4.0
Provides:       bundled(npm(base64-js)) = 1.5.1
Provides:       bundled(npm(buffer)) = 6.0.3
Provides:       bundled(npm(ieee754)) = 1.2.1
Provides:       bundled(npm(jupyterlab-rise)) = 0.41.0

%description -n python3-jupyterlab-jupytext %_desc

%package        doc
# The content is MIT.  Other licenses are due to Sphinx files.
# _static/alabaster.css: BSD-3-Clause
# _static/basic.css: BSD-2-Clause
# _static/check-solid.svg: MIT
# _static/clipboard.min.js: MIT
# _static/copy-button.svg: MIT
# _static/copybutton.css: MIT
# _static/copybutton.js: MIT
# _static/copybutton_funcs.js: MIT
# _static/custom.css: BSD-3-Clause
# _static/doctools.js: BSD-2-Clause
# _static/documentation_options.js: BSD-2-Clause
# _static/file.png: BSD-2-Clause
# _static/language_data.js: BSD-2-Clause
# _static/logo.svg: MIT
# _static/minus.png: BSD-2-Clause
# _static/plus.png: BSD-2-Clause
# _static/pygments.css: MIT
# _static/searchtools.js: BSD-2-Clause
# _static/sphinx_highlight.js: BSD-2-Clause
# genindex.html: BSD-2-Clause
# search.html: BSD-2-Clause
# searchindex.js: BSD-2-Clause
License:        MIT AND BSD-3-Clause AND BSD-2-Clause
Summary:        Documentation for %{name}

%description    doc
Documentation for %{name}.

%prep
%autosetup -n jupytext-%{version} -p1
tar -C jupyterlab -xf %{SOURCE1}
cp -p %{SOURCE2} .

# Remove spurious executable bits
chmod a-x README.md

# Take this package out of the doc requirements
sed -i '/jupytext/d' docs/doc-requirements.txt

# Take this package out of the test requirements
sed -ri '/jupytext\[test(-functional)?\]/d' pyproject.toml

%generate_buildrequires
export HATCH_BUILD_HOOKS_ENABLE=true
%pyproject_buildrequires -x docs,test,test-functional,test-integration

%build
export HATCH_BUILD_HOOKS_ENABLE=true
export YARN_CACHE_FOLDER="$PWD/jupyterlab/.package-cache"
export npm_config_nodedir=%{_includedir}/node
export CFLAGS='%{build_cflags} -I%{_includedir}/node'
export CXXFLAGS='%{build_cxxflags} -I%{_includedir}/node'

%pyproject_wheel

# Build the documentation
PYTHONPATH=$PWD %make_build -C docs html
rm docs/_build/html/.buildinfo

%install
export HATCH_BUILD_HOOKS_ENABLE=true
%pyproject_install
%pyproject_save_files -l jupytext jupytext_config

# Cleanup backup files
find %{buildroot}%{_prefix} -name \*.orig -delete

# Move the configuration files to the standard Jupyter directories
mv %{buildroot}%{_prefix}%{_sysconfdir} %{buildroot}%{_sysconfdir}

# Link rather than copy the labextension
rm -fr %{buildroot}%{python3_sitelib}/jupyterlab_jupytext/labextension
ln -s %{_datadir}/jupyter/labextensions/jupyterlab-jupytext \
  %{buildroot}%{python3_sitelib}/jupyterlab_jupytext/labextension

# Generate man pages
mkdir -p %{buildroot}%{_mandir}/man1
export PYTHONPATH=%{buildroot}%{python3_sitelib}
help2man -N -n 'Save Jupyter notebooks as text documents or scripts' \
  %{buildroot}%{_bindir}/jupytext -o %{buildroot}%{_mandir}/man1/jupytext.1
help2man -N -n 'Manage jupytext configuration' --version-string=%{version} \
  %{buildroot}%{_bindir}/jupytext-config \
  -o %{buildroot}%{_mandir}/man1/jupytext-config.1

%check
# Skip the external tests, which require network access
%pytest --ignore=tests/external

%files -n python3-jupytext -f %{pyproject_files}
%doc README.md
%{_bindir}/jupytext
%{_bindir}/jupytext-config
%{_mandir}/man1/jupytext.1*
%{_mandir}/man1/jupytext-config.1*
%config(noreplace) %{_sysconfdir}/jupyter/jupyter_notebook_config.d/jupytext.json
%config(noreplace) %{_sysconfdir}/jupyter/jupyter_server_config.d/jupytext.json

%files -n python3-jupyterlab-jupytext
%{python3_sitelib}/jupyterlab_jupytext/
%{_datadir}/jupyter/labextensions/jupyterlab-jupytext/

%files doc
%doc docs/_build/html
%license LICENSE jupytext-%{version}-vendor-licenses.txt

%changelog
%autochangelog
