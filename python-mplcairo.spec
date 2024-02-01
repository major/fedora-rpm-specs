%global srcname mplcairo

Name:           python-%{srcname}
Version:        0.5
Release:        %autorelease
Summary:        A (new) cairo backend for Matplotlib

License:        MIT
URL:            https://github.com/matplotlib/mplcairo
Source0:        %pypi_source %{srcname}
# Make pth-generation PEP517-compatible.
# https://github.com/matplotlib/mplcairo/commit/bf3b69ceec82b09350e725d310e3a324afc0c3ff
Patch:          0001-Make-pth-generation-PEP517-compatible.patch
# Fix use with latest wheel.
# https://github.com/matplotlib/mplcairo/commit/e85ebb2115f617e20c0269047f9b50ac050f5eb9
Patch:          0002-Remove-fragile-build_ext-command-run-order-check.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  gcc-c++

%description
This is a new, essentially complete implementation of a cairo backend for
Matplotlib. It can be used in combination with a Qt5, GTK3, Tk, wx, or macOS
UI, or noninteractively (i.e., to save figure to various file formats).
Noteworthy points include:
  - Improved accuracy (e.g., with marker positioning, quad meshes, and text
    kerning).
  - Support for a wider variety of font formats, such as otf and pfb, for vector
    (PDF, PS, SVG) backends (Matplotlib's Agg backend also supports such fonts).
  - Optional support for complex text layout (right-to-left languages, etc.)
    using Raqm.
  - Support for embedding URLs in PDF (but not SVG) output.
  - Support for multi-page output both for PDF and PS (Matplotlib only supports
    multi-page PDF).
  - Support for custom blend modes (see `examples/operators.py`).


%package -n     python3-%{srcname}
Summary:        %{summary}

BuildRequires:  pkgconfig(cairo) >= 1.15.4
BuildRequires:  freetype-devel
BuildRequires:  pkgconfig(raqm) >= 0.7.0
BuildRequires:  python3-devel
BuildRequires:  python3-matplotlib-test-data >= 2.2
BuildRequires:  python3dist(pytest) >= 3.2.2
BuildRequires:  python3dist(pytest-xdist)
BuildRequires:  python3dist(sphinx)

BuildRequires:  font(dejavusans)
BuildRequires:  font(notosanscjkjp)
BuildRequires:  font(wenquanyizenhei)

# LaTeX dependencies for tests, copied from python-matplotlib.
BuildRequires:  texlive-collection-basic
BuildRequires:  texlive-collection-fontsrecommended
BuildRequires:  texlive-collection-latex
BuildRequires:  texlive-collection-latexrecommended
BuildRequires:  texlive-dvipng
BuildRequires:  texlive-latex-bin
BuildRequires:  texlive-luahbtex
BuildRequires:  texlive-tex-bin
BuildRequires:  texlive-xetex-bin
# Search for documentclass and add the classes here.
BuildRequires:  tex(article.cls)
# Search for inputenc and add any encodings used with it.
BuildRequires:  tex(utf8.def)
BuildRequires:  tex(utf8x.def)
# Found with: rg -Io 'usepackage(\[.+\])?\{.+\}' lib | rg -o '\{.+\}' | sort -u
# and then removing duplicates in one line, etc.
BuildRequires:  tex(avant.sty)
BuildRequires:  tex(chancery.sty)
BuildRequires:  tex(charter.sty)
BuildRequires:  tex(chemformula.sty)
BuildRequires:  tex(color.sty)
BuildRequires:  tex(courier.sty)
BuildRequires:  tex(fontenc.sty)
BuildRequires:  tex(fontspec.sty)
BuildRequires:  tex(geometry.sty)
BuildRequires:  tex(graphicx.sty)
BuildRequires:  tex(helvet.sty)
BuildRequires:  tex(hyperref.sty)
BuildRequires:  tex(import.sty)
BuildRequires:  tex(inputenc.sty)
BuildRequires:  tex(lmodern.sty)
BuildRequires:  tex(mathpazo.sty)
BuildRequires:  tex(mathptmx.sty)
BuildRequires:  tex(pgf.sty)
BuildRequires:  tex(sfmath.sty)
BuildRequires:  tex(textcomp.sty)
BuildRequires:  tex(txfonts.sty)
BuildRequires:  tex(type1cm.sty)
BuildRequires:  tex(type1ec.sty)
BuildRequires:  tex(underscore.sty)
# See BakomaFonts._fontmap in lib/matplotlib/mathtext.py
BuildRequires:  tex(cmb10.tfm)
BuildRequires:  tex(cmex10.tfm)
BuildRequires:  tex(cmmi10.tfm)
BuildRequires:  tex(cmr10.tfm)
BuildRequires:  tex(cmss10.tfm)
BuildRequires:  tex(cmsy10.tfm)
BuildRequires:  tex(cmtt10.tfm)

Requires:       cairo >= 1.15.4
Requires:       libraqm >= 0.7.0

%description -n python3-%{srcname}
This is a new, essentially complete implementation of a cairo backend for
Matplotlib. It can be used in combination with a Qt5, GTK3, Tk, wx, or macOS
UI, or noninteractively (i.e., to save figure to various file formats).
Noteworthy points include:
  - Improved accuracy (e.g., with marker positioning, quad meshes, and text
    kerning).
  - Support for a wider variety of font formats, such as otf and pfb, for vector
    (PDF, PS, SVG) backends (Matplotlib's Agg backend also supports such fonts).
  - Optional support for complex text layout (right-to-left languages, etc.)
    using Raqm.
  - Support for embedding URLs in PDF (but not SVG) output.
  - Support for multi-page output both for PDF and PS (Matplotlib only supports
    multi-page PDF).
  - Support for custom blend modes (see `examples/operators.py`).


%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
# We need to prime this LaTeX cache stuff, or it might fail while running tests
# in parallel.
mktexfmt latex.fmt
mktexfmt lualatex.fmt
mktexfmt pdflatex.fmt
mktexfmt xelatex.fmt

export PYTHONPATH="%{buildroot}%{python3_sitearch}" PYTHONDONTWRITEBYTECODE=1

%{python3} -c 'import mplcairo.base'

MPLBACKEND=module://mplcairo.base %{python3} - <<EOF
import matplotlib.pyplot as plt
print(plt.get_backend())
fig, ax = plt.subplots()
fig.savefig("/dev/null", format="png")
EOF

# 50 is upstream recommended tolerance since results won't match MPL exactly.
%{python3} run-mpl-test-suite.py --tolerance=50 -m 'not network' -v -n auto \
    -k 'not test_backends_interactive'

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt
%{python3_sitearch}/%{srcname}.pth

%changelog
%autochangelog
