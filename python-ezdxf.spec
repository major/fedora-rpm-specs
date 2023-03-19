# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond_without doc_pdf

# As of 2022-12-12, PySide6 (https://pypi.org/project/PySide6/) is not yet
# packaged in Fedora. When it is, we should use it.
%bcond_with qt6

Name:           python-ezdxf
Version:        1.0.2
Release:        %autorelease
Summary:        Create/manipulate DXF drawings

# The entire source is MIT, except:
#
# - The following are derived from https://github.com/mapbox/earcut (but are a
#   rewrite from C++ to Python, so are not treated as a bundled dependency) and
#   are therefore (ISC AND MIT):
#     * src/ezdxf/acc/mapbox_earcut.pyx
#     * src/ezdxf/math/_mapbox_earcut.py
# - The following is derived from
#   https://github.com/mlarocca/AlgorithmsAndDataStructuresInAction/tree/master/JavaScript/src/ss_tree
#   (but is a rewrite from JavaScript to Python, so is not treated as a bundled
#   dependency) and is therefore (AGPL-3.0-only AND MIT):
#     * src/ezdxf/math/rtree.py
#
# Additionally:
# - The following is derived from https://github.com/enzoruiz/3dbinpacking.
#   Since the original source is Python, it is treated as a bundled dependency;
#   since the implementation is forked, it cannot be unbundled. The original
#   source is also under an (MIT) license, so this does not affect the License
#   tag.
#     * ezdxf/addons/binpacking.py
#
# Finally, the following are removed in %%prep and do not contribute to the
# licenses of the binary RPMs:
# - The following are Apache-2.0:
#     * fonts/Open_Sans/
#     * fonts/Open_Sans_Condensed/
# - The following are OFL-1.0
#     * fonts/liberation-fonts-ttf-2.00.4/
#     * fonts/liberation-fonts-ttf-2.1.1/
License:        MIT AND ISC AND AGPL-3.0-only
URL:            https://ezdxf.mozman.at/
%global forgeurl https://github.com/mozman/ezdxf
Source0:        %{forgeurl}/archive/v%{version}/ezdxf-%{version}.tar.gz

# Man pages written for Fedora in groff_man(7) format based on --help output
# and docs/ content.
Source10:       ezdxf.1
Source11:       ezdxf-audit.1
Source12:       ezdxf-browse.1
Source13:       ezdxf-browse-acis.1
Source14:       ezdxf-config.1
Source15:       ezdxf-draw.1
Source16:       ezdxf-info.1
Source17:       ezdxf-pillow.1
Source18:       ezdxf-pp.1
Source19:       ezdxf-strip.1
Source20:       ezdxf-view.1

BuildRequires:  python3-devel
BuildRequires:  gcc-c++

BuildRequires:  dos2unix

# Standard styles use OpenSans and Liberation fonts; see
# src/ezdxf/tools/standards.py
BuildRequires:  font(opensans)
BuildRequires:  font(opensansextrabold)
BuildRequires:  font(opensanslight)
BuildRequires:  font(opensanssemibold)
BuildRequires:  font(liberationmono)
BuildRequires:  font(liberationsans)
BuildRequires:  font(liberationsansnarrow)
BuildRequires:  font(liberationserif)
%if 0%{?fedora} > 38
# No longer available: font(notosanssc)
# https://bugzilla.redhat.com/show_bug.cgi?id=2179387
%else
# This is used in tests/test_08_addons/test_814_text2path.py. (The test is
# simply skipped if the font is not present.)
BuildRequires:  font(notosanssc)
%endif

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
BuildRequires:  /usr/bin/xindy
BuildRequires:  tex-xetex-bin
BuildRequires:  /usr/bin/rsvg-convert
%endif

%global common_description %{expand:
This Python package is for creating and modifying DXF documents, regardless of
the DXF version. The package supports loading and rewriting DXF file without
losing any content except comments. Unknown DXF tags in the document are
ignored but kept for rewriting. This behavior allows processing DXF documents
that contain data from third-party applications without loosing information.}

%description %{common_description}


%package -n     python3-ezdxf
Summary:        %{summary}

Requires:       font(opensans)
Requires:       font(opensansextrabold)
Requires:       font(opensanslight)
Requires:       font(opensanssemibold)
Requires:       font(liberationmono)
Requires:       font(liberationsans)
Requires:       font(liberationsansnarrow)
Requires:       font(liberationserif)

# See the note above the %%pyproject_extras_subpkg invocation.
Obsoletes:      python3-ezdxf+all < 0.17.2-7
Obsoletes:      python3-ezdxf+all < 0.17.2-7

# ezdxf/addons/binpacking.py is derived from an unspecified version of py3dbp
# (https://github.com/enzoruiz/3dbinpacking, https://pypi.org/project/py3dbp/).
# The implementation is significantly forked, so unbundling will not be
# possible.
Provides:       bundled(python3dist(py3dbp))

%description -n python3-ezdxf %{common_description}


# Note extra “all” is “draw”+“dev”+“test”, and “all5” is “draw5”+“dev”+“test”.
# Since it does not really make sense to package extras metapackages for dev
# and test dependencies, we omit these two extras as well.
%pyproject_extras_subpkg -n python3-ezdxf %{?with_qt6:draw},draw5


%package        doc
Summary:        Documentation for ezdxf

BuildArch:      noarch

%description    doc %{common_description}


%prep
%autosetup -n ezdxf-%{version} -p1
# Note that C++ sources in the GitHub tarball are *not* Cython-generated, and
# we must not remove them.

# Remove bundled fonts; these would not be installed anyway.
rm -rvf fonts/

# Since pdflatex cannot handle Unicode inputs in general:
echo "latex_engine = 'xelatex'" >> docs/source/conf.py
rm docs/graphics/dimtad-dimjust.pdf

# Fix files with CRNL newlines and, in some cases, UTF-16LE encoding:
dos2unix docs/notes/dxf-group-code-reference.txt \
    examples/copydxf.py \
    examples_dxf/text.dxf \
    examples_dxf/text_negative_extrusion.dxf

# qtviewer.py is not executable and is not script-like (no main routine or
# useful side effects), so it does not need a shebang
sed -r -i '1{/^#!/d}' src/ezdxf/addons/drawing/qtviewer.py

# A couple of examples are installed as executables, with shebangs that need to
# be corrected.
%py3_shebang_fix examples

# We don’t need to run typecheckers, and we must build documentation with
# whichever sphinx-rtd-theme version we have.
sed -r \
    -e 's/^(typing_extensions%{?!with_qt6:|pyside6})\b/# \1/' \
    -e 's/^(sphinx-rtd-theme)<.*$/\1/' \
    requirements-dev.txt | tee requirements-dev-filtered.txt


%generate_buildrequires
# Note extra “all” is “draw”+“dev”+“test”, and “all5” is “draw5”+“dev”+“test”.
%pyproject_buildrequires -x all%{?!with_qt6:5} requirements-dev-filtered.txt


%build
%pyproject_wheel

%if %{with doc_pdf}
# Cannot use SVG images when building PDF documentation; convert to PDFs
find docs -type f -name '*.svg' |
  while read -r fn
  do
    rsvg-convert --format=pdf "${fn}" \
        --output="$(dirname "${fn}")/$(basename "${fn}" .svg).pdf"
  done
find docs/source -type f -exec \
    gawk '/\.svg/ { print FILENAME; nextfile }' '{}' '+' |
  xargs -r -t sed -r -i 's/\.svg/\.pdf/g'

BLIB="${PWD}/build/lib.%{python3_platform}-cpython-%{python3_version_nodots}"
PYTHONPATH="${BLIB}" %make_build -C docs -f Makefile.linux latex \
    SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/build/latex LATEXMKOPTS='-quiet'
%endif


%install
%pyproject_install
%pyproject_save_files ezdxf

install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 \
    '%{SOURCE10}' '%{SOURCE11}' '%{SOURCE12}' '%{SOURCE13}' '%{SOURCE14}' \
    '%{SOURCE15}' '%{SOURCE16}' '%{SOURCE17}' '%{SOURCE18}' '%{SOURCE19}' \
    '%{SOURCE20}'


%check
# No need to set EZDXF_TEST_FILES because the files in question are not
# available (and are presumably not freely distributable). This is fine; it
# just means a few tests are automatically skipped.

# See tox-extras.ini:
# Note: It is NOT safe to parallelize these tests with pytest-xdist!
%pytest -k "${k-}" tests integration_tests

# Since the user can disable the C extensions, test the pure-Python
# implementations too:
EZDXF_DISABLE_C_EXT=1 %pytest -k "${k-}" tests integration_tests

%files -n python3-ezdxf -f %{pyproject_files}
# pyproject-rpm-macros handles the LICENSE file; verify with “rpm -qL -p …”
%doc README.md

%{_bindir}/ezdxf
%{_mandir}/man1/ezdxf*.1*


%files doc
%license LICENSE

%doc NEWS*.md
%doc README.md
%doc TODO.md

%doc autolisp
%doc examples
%doc examples_dxf
%doc exploration
%doc docs/notes

%if %{with doc_pdf}
%doc docs/build/latex/ezdxf.pdf
%endif


%changelog
%autochangelog
