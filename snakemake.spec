# Work around a series of circular test dependencies:
#
#    python-snakemake-interface-report-plugins
#    ￬￪   ⬐───╮
# snakemake → python-snakemake-interface-executor-plugins⬎
#    ￪￪ │ ⬑────────────────────python-snakemake-executor-plugin-cluster-generic
#    ││ ↳python-snakemake-interface-storage-plugins────────────────╮
#    ││                                           ￬                │
#    │╰────────────────────────python-snakemake-storage-plugin-http│
#    ╰─────────────────────────python-snakemake-storage-plugin-s3🠔─╯
#
# A good build order is:
#
#   1. BOOTSTRAP: python-snakemake-interface-executor-plugins,
#      python-snakemake-interface-storage-plugins,
#      python-snakemake-interface-report-plugins
#   2. BOOTSTRAP: snakemake
#   3. python-snakemake-executor-plugin-cluster-generic,
#      python-snakemake-storage-plugin-http,
#      python-snakemake-storage-plugin-s3
#   4. snakemake, python-snakemake-interface-executor-plugins,
#      python-snakemake-interface-storage-plugins,
#      python-snakemake-interface-report-plugins
%bcond bootstrap 0
%bcond tests %{without bootstrap}

%global _description %{expand:
The Snakemake workflow management system is a tool to create reproducible and
scalable data analyses. Workflows are described via a human readable, Python
based language. They can be seamlessly scaled to server, cluster, grid and
cloud environments, without the need to modify the workflow definition.
Finally, Snakemake workflows can entail a description of required software,
which will be automatically deployed to any execution environment.}

Name:           snakemake
Version:        8.5.4
Release:        %autorelease 
Summary:        Workflow management system to create reproducible and scalable data analyses

# The entire project is (SPDX) MIT, except:
# - versioneer.py is Unlicense
# - snakemake/_version.py says:
#     This file is released into the public domain.
#   which would be LicenseRef-Fedora-Public-Domain, except that the comments in
#   versioneer.py make it clear that Unlicense is intended for the generated
#   files as well.
License:        MIT AND Unlicense
URL:            https://snakemake.readthedocs.io/en/stable/index.html
Source:         https://github.com/snakemake/snakemake/archive/v%{version}/snakemake-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

BuildRequires:  help2man

BuildRequires:  vim-filesystem
Requires:       vim-filesystem

Provides:       vim-snakemake = %{version}-%{release}
# These extras were removed upstream in Snakemake 8.0.0. Retain the Obsoletes
# until F40 reaches EOL so we have a clean upgrade path.
Obsoletes:      snakemake+azure < 8.1.0-1
Obsoletes:      snakemake+google-cloud < 8.1.0-1
# We no longer build Sphinx-generated PDF documentation. Beginning with 8.2.3,
# this would require patching out sphinxawesome-theme from docs/conf.py. It’s
# possible but tedious.
Obsoletes:      snakemake-doc < 8.2.1-2

%if %{with tests}
# See test-environment.yml for a listing of test dependencies, along with a lot
# of other cruft.
BuildRequires:  %{py3_dist boto3}
BuildRequires:  %{py3_dist pandas}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist snakemake-executor-plugin-cluster-generic}
BuildRequires:  %{py3_dist snakemake-storage-plugin-s3}
%endif
# For import-testing snakemake.gui
BuildRequires:  %{py3_dist flask}
# For import-testing snakemake.executors.google_lifesciences_helper:
BuildRequires:  %{py3_dist google-cloud-storage}

%description %_description

# No metapackage for “pep” extra because the following are not packaged:
#   - python3-eido
#   - python3-peppy
%pyproject_extras_subpkg -n snakemake reports messaging

%prep
%autosetup -n snakemake-%{version} -p1
%py3_shebang_fix .
# Remove shebangs from non-executable scripts. The Python script is executable
# in the source tree but will be installed without executable permissions.
sed -r -i '1{/^#!/d}' \
    snakemake/executors/jobscript.sh \
    snakemake/executors/google_lifesciences_helper.py
# Fix calls to unversioned Python interpreter
sed -r -i 's@"python"@"%{python3}"@g' tests/test_linting.py
sed -r -i 's@python -m@"%{python3} -m@g' tests/tests.py
# Copy and rename nano and vim extensions readmes for use in the main
# documentation directory.
for editor in nano vim
do
  cp -vp "misc/${editor}/README.md" "README-${editor}.md"
done

%generate_buildrequires
# Generate BR’s for all supported extras to ensure they do not FTI
%pyproject_buildrequires -x reports,messaging,google-cloud,azure

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l snakemake

# We wait until %%install to generate the man page so that we can use the
# proper script entry point. The generated man page is not perfect, but it is
# good enough to be useful.
install -d %{buildroot}%{_mandir}/man1
PATH="${PATH-}:%{buildroot}%{_bindir}" \
    PYTHONPATH='%{buildroot}%{python3_sitelib}' \
    help2man --no-info --name='%{summary}' snakemake \
    > %{buildroot}%{_mandir}/man1/snakemake.1

# Install nano syntax highlighting
install -t '%{buildroot}%{_datadir}/nano' -D -m 0644 -p \
    misc/nano/syntax/snakemake.nanorc

# Install vim syntax highlighting
install -d '%{buildroot}%{_datadir}/vim/vimfiles'
cp -vrp misc/vim/* '%{buildroot}%{_datadir}/vim/vimfiles'
find '%{buildroot}%{_datadir}/vim/vimfiles' \
    -type f -name 'README.*' -print -delete

%check
# Even if we are running the tests, this is useful; it could turn up import
# errors that would only be revealed by tests we had to disable (e.g. due to
# network access).
#
# ImportError from snakemake.executors.flux (no 'sleep' in
# snakemake_interface_executor_plugins.utils)
# https://github.com/snakemake/snakemake/issues/2598
# “The flux module is actually supposed to be moved into a plugin and has no
# connection to the rest of the code anymore.”
%pyproject_check_import -e '*.tests*' -e 'snakemake.executors.flux'

%if %{with tests}
# Needs a network connection:
ignore="${ignore-} --ignore-glob=tests/test_google_lifesciences/*"

# Needs a network connection (plus, there are some unresolved
# unversioned-python-command issues which we hope are confined to the test
# code):
k="${k-}${k+ and }not test_deploy_sources"

# ______ ERROR collecting tests/test_conda_python_script/test_script.py ______
# import file mismatch:
# imported module 'test_script' has this __file__ attribute:
#   /builddir/build/BUILD/snakemake-7.31.1/tests/test_conda_python_3_7_script/test_script.py
# which is not the same as the test file we want to collect:
#   /builddir/build/BUILD/snakemake-7.31.1/tests/test_conda_python_script/test_script.py
# HINT: remove __pycache__ / .pyc files and/or use a unique basename for your test file modules
#
# Plus, this would add an unwanted BuildRequires on %%{py3_dist Pillow}.
ignore="${ignore-} --ignore-glob=tests/test_conda_python_3_7_script/*"

%pytest -v -k "${k-}" ${ignore-}
%endif

%files -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md
%doc README-nano.md
%doc README-vim.md

%{_bindir}/snakemake
%{_mandir}/man1/snakemake.1*

# This is not owned by the filesystem package, and there is no nano-filesystem
# subpackage, so we co-own the directory to avoid depending on nano.
%dir %{_datadir}/nano/
%{_datadir}/nano/snakemake.nanorc

%{_datadir}/vim/vimfiles/ftdetect/snakemake.vim
%{_datadir}/vim/vimfiles/ftplugin/snakemake/
%{_datadir}/vim/vimfiles/syntax/snakemake.vim

%changelog
%autochangelog
