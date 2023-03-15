%bcond_without tests
# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
%bcond_without doc_pdf

%global _description %{expand:
The Snakemake workflow management system is a tool to create reproducible and
scalable data analyses. Workflows are described via a human readable, Python
based language. They can be seamlessly scaled to server, cluster, grid and
cloud environments, without the need to modify the workflow definition.
Finally, Snakemake workflows can entail a description of required software,
which will be automatically deployed to any execution environment.}

Name:           snakemake
Version:        7.24.1
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
Source0:        https://github.com/snakemake/snakemake/archive/v%{version}/snakemake-%{version}.tar.gz

BuildArch:      noarch

# Since we build the docs as a PDF, we can’t include an animated GIF demo.
# Patch out the image reference and the text referring to it.
Patch:          snakemake-7.11.0-docs-no-animated-demo.patch

BuildRequires:  python3-devel

%if %{with tests}
# See test-environment.yml for a listing of test dependencies, along with a lot
# of other cruft.
BuildRequires:  %{py3_dist boto3}
BuildRequires:  %{py3_dist configargparse}
# For tests/test_google_lifesciences.py; but it would need a network connection
#BuildRequires:  %%{py3_dist google-api-python-client}
#BuildRequires:  %%{py3_dist google-cloud-storage}
BuildRequires:  %{py3_dist pandas}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist requests-mock}
%endif

%description %_description

%package doc

Summary:        %{summary}

BuildArch:      noarch

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
BuildRequires:  tex-xetex-bin
BuildRequires:  /usr/bin/xindy
BuildRequires:  /usr/bin/rsvg-convert
%endif

%description doc %_description

# No metapackage for “pep” extra because the following are not packaged:
#   - python3-eido
#   - python3-peppy
%pyproject_extras_subpkg -n snakemake reports messaging google-cloud

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
# Now part of Sphinx:
sed -r -i '/sphinxcontrib-napoleon/d' docs/requirements.txt
# Since pdflatex cannot handle Unicode inputs in general:
echo "latex_engine = 'xelatex'" >> docs/conf.py

%generate_buildrequires
# Generate BR’s for all supported extras to ensure they do not FTI
%pyproject_buildrequires -x reports,messaging,google-cloud %{?with_doc_pdf:docs/requirements.txt}

%build
%pyproject_wheel
%if %{with doc_pdf}
# Cannot use SVG images when building PDF documentation; convert to PDFs
find docs -type f -name '*.svg' |
  while read -r fn
  do
    rsvg-convert --format=pdf \
        --output="$(dirname "${fn}")/$(basename "${fn}" .svg).pdf" "${fn}"
  done
find docs/executor_tutorial -type f -exec \
    gawk '/\.svg/ { print FILENAME; nextfile }' '{}' '+' |
  xargs -r -t sed -r -i 's/(image::.*)\.svg/\1\.pdf/'
PYTHONPATH="${PWD}" %make_build -C docs latexpdf SPHINXOPTS='%{?_smp_mflags}'
%endif

%install
%pyproject_install
%pyproject_save_files snakemake

%check
%if %{with tests}
# Lint output “Migrate long run directives into scripts or notebooks …” is
# apparently not expected by upstream
k="${k-}${k+ and }not test_lint[long_run-positive]"
# Needs a network connection
k="${k-}${k+ and }not test_tibanna"
# Requires py-tes. Currently not packaged for Fedora.
k="${k-}${k+ and }not test_tes"
# Require a running slurm instance; maybe this is possible to set up
# temporarily in the offline build environment, but we don’t know how.
k="${k-}${k+ and }not test_slurm_"
# tests/test_google_lifesciences.py needs a network connection (and GCP credentials)
%pytest -v -k "${k-}" --ignore tests/test_google_lifesciences.py
%endif

%files -f %{pyproject_files}
%{_bindir}/snakemake
%{_bindir}/snakemake-bash-completion

%files doc
%license LICENSE.md
%doc CHANGELOG.md
%doc CODE_OF_CONDUCT.md
%doc README.md
%if %{with doc_pdf}
%doc docs/_build/latex/Snakemake.pdf
%endif

%changelog
%autochangelog
