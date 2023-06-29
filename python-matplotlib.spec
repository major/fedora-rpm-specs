%bcond_with html
%bcond_without check
# https://fedorahosted.org/fpc/ticket/381
%bcond_without bundled_fonts

# No WX for EL8/ELN/EL9
%if 0%{?rhel} >= 8
%bcond_with wx
%else
%bcond_without wx
%endif

# the default backend; one of GTK3Agg GTK3Cairo MacOSX Qt4Agg Qt5Agg TkAgg
# WXAgg Agg Cairo PS PDF SVG
%global backend                 TkAgg

%if "%{backend}" == "TkAgg"
%global backend_subpackage tk
%else
%  if "%{backend}" == "Qt5Agg"
%global backend_subpackage qt5
%  else
%    if "%{backend}" == "WXAgg"
%global backend_subpackage wx
%    endif
%  endif
%endif

# Use the same directory of the main package for subpackage licence and docs
%global _docdir_fmt %{name}

# Updated test images for new FreeType.
%global mpl_images_version 3.7.1

# The version of FreeType in this Fedora branch.
%global ftver 2.12.1

Name:           python-matplotlib
Version:        3.7.1
%global Version 3.7.1
Release:        %autorelease
Summary:        Python 2D plotting library
# qt_editor backend is MIT
# ResizeObserver at end of lib/matplotlib/backends/web_backend/js/mpl.js is CC0
License:        PSF-2.0 and MIT and CC0-1.0
URL:            https://matplotlib.org
Source0:        %pypi_source matplotlib %{Version}
Source1:        mplsetup.cfg

# Fedora-specific patches; see:
# https://github.com/fedora-python/matplotlib/tree/fedora-patches
# Updated test images for new FreeType.
Source1000:     https://github.com/QuLogic/mpl-images/archive/v%{mpl_images_version}-with-freetype-%{ftver}/matplotlib-%{mpl_images_version}-with-freetype-%{ftver}.tar.gz
# Search in /etc/matplotlibrc:
Patch1001:      0001-matplotlibrc-path-search-fix.patch
Patch1002:      0002-Don-t-require-oldest-supported-numpy.patch
# Increase tolerances for new FreeType everywhere:
Patch1003:      0003-Set-FreeType-version-to-%{ftver}-and-update-tolerances.patch

# https://github.com/matplotlib/matplotlib/pull/21190#issuecomment-1223271888
Patch0001:      0004-Use-old-stride_windows-implementation-on-32-bit-x86.patch
# https://github.com/matplotlib/matplotlib/pull/25068
Source2000:     pgf_pdflatex.pdf
Source2001:     pgf_rcupdate2.pdf
# https://github.com/matplotlib/matplotlib/pull/25918
Patch0002:      0006-migrate-from-utcfromtimestamp-to-fromtimestamp-25918.patch
# https://github.com/matplotlib/matplotlib/pull/26154
Patch0003:      0007-MNT-py312-deprecates-pickling-objects-in-itertools.patch
# https://github.com/matplotlib/matplotlib/pull/26165
Patch0004:      0008-Avoid-Py_VerboseFlag-deprecation-from-Python-3.12.patch
Patch0005:      0009-Skip-tests-failing-with-Python-3.12.0b3.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glibc-langpack-en
BuildRequires:  freetype-devel
BuildRequires:  libpng-devel
BuildRequires:  qhull-devel
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  zlib-devel

BuildRequires:  ghostscript
# No ImageMagick for EL8/ELN/EL9
%if 0%{?fedora} || (0%{?rhel} && 0%{?rhel} < 8)
BuildRequires:  ImageMagick
%endif
BuildRequires:  inkscape

BuildRequires:  font(dejavusans)
BuildRequires:  font(notosanscjkjp)
BuildRequires:  font(wenquanyizenhei)

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

%description
Matplotlib is a Python 2D plotting library which produces publication
quality figures in a variety of hardcopy formats and interactive
environments across platforms. Matplotlib can be used in Python
scripts, the Python and IPython shell, web application servers, and
various graphical user interface toolkits.

Matplotlib tries to make easy things easy and hard things possible.
You can generate plots, histograms, power spectra, bar charts,
errorcharts, scatterplots, etc, with just a few lines of code.

%package -n python3-matplotlib-data
Summary:        Data used by python-matplotlib
BuildArch:      noarch
%if %{with bundled_fonts}
Requires:       python3-matplotlib-data-fonts = %{version}-%{release}
%endif
Obsoletes:      python-matplotlib-data < 3

%description -n python3-matplotlib-data
%{summary}

%if %{with bundled_fonts}
%package -n python3-matplotlib-data-fonts
Summary:        Fonts used by python-matplotlib
# Carlogo, STIX and Computer Modern is OFL
# DejaVu is Bitstream Vera and Public Domain
License:        OFL-1.1 and Bitstream-Vera and LicenseRef-Fedora-Public-Domain
BuildArch:      noarch
Requires:       python3-matplotlib-data = %{version}-%{release}
Obsoletes:      python-matplotlib-data-fonts < 3

%description -n python3-matplotlib-data-fonts
%{summary}
%endif

%package -n     python3-matplotlib
Summary:        Python 2D plotting library
BuildRequires:  python3-devel
BuildRequires:  python3dist(pycairo)
BuildRequires:  python3dist(pytz)
BuildRequires:  python3dist(sphinx)
Requires:       dejavu-sans-fonts
Recommends:     texlive-dvipng
Requires:       (texlive-dvipng if texlive-base)
Requires:       python3-matplotlib-data = %{version}-%{release}
Requires:       python3dist(pycairo)
Requires:       python3-matplotlib-%{?backend_subpackage}%{!?backend_subpackage:tk}%{?_isa} = %{version}-%{release}
%if %{with check}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-rerunfailures)
BuildRequires:  python3dist(pytest-timeout)
BuildRequires:  python3dist(pytest-xdist)
BuildRequires:  python3dist(pikepdf)
%endif
%if %{without bundled_fonts}
Requires:       stix-math-fonts
%else
Provides:       bundled(stix-math-fonts)
%endif

%description -n python3-matplotlib
Matplotlib is a Python 2D plotting library which produces publication
quality figures in a variety of hardcopy formats and interactive
environments across platforms. Matplotlib can be used in Python
scripts, the Python and IPython shell, web application servers, and
various graphical user interface toolkits.

Matplotlib tries to make easy things easy and hard things possible.
You can generate plots, histograms, power spectra, bar charts,
errorcharts, scatterplots, etc, with just a few lines of code.

%package -n     python3-matplotlib-qt5
Summary:        Qt5 backend for python3-matplotlib
BuildRequires:  python3dist(cairocffi)
BuildRequires:  python3dist(pyqt5)
Requires:       python3-matplotlib%{?_isa} = %{version}-%{release}
Requires:       python3dist(cairocffi)
Requires:       python3dist(pyqt5)
Obsoletes:      python3-matplotlib-qt4 < 3.5.0-0

%description -n python3-matplotlib-qt5
%{summary}

%package -n     python3-matplotlib-qt6
Summary:        Qt6 backend for python3-matplotlib
BuildRequires:  python3dist(cairocffi)
BuildRequires:  python3dist(pyqt6)
Requires:       python3-matplotlib%{?_isa} = %{version}-%{release}
Requires:       python3dist(cairocffi)
Requires:       python3dist(pyqt6)

%description -n python3-matplotlib-qt6
%{summary}

%package -n     python3-matplotlib-gtk3
Summary:        GTK3 backend for python3-matplotlib
# This should be converted to typelib(Gtk) when supported
BuildRequires:  gtk3
BuildRequires:  python3-gobject
Requires:       gtk3%{?_isa}
Requires:       python3-gobject%{?_isa}
Requires:       python3-matplotlib%{?_isa} = %{version}-%{release}

%description -n python3-matplotlib-gtk3
%{summary}

%package -n     python3-matplotlib-gtk4
Summary:        GTK4 backend for python3-matplotlib
# This should be converted to typelib(Gtk) when supported
BuildRequires:  gtk4
BuildRequires:  python3-gobject
Requires:       gtk4%{?_isa}
Requires:       python3-gobject%{?_isa}
Requires:       python3-matplotlib%{?_isa} = %{version}-%{release}

%description -n python3-matplotlib-gtk4
%{summary}

%package -n     python3-matplotlib-tk
Summary:        Tk backend for python3-matplotlib
BuildRequires:  python3-pillow-tk
BuildRequires:  python3-tkinter
Requires:       python3-matplotlib%{?_isa} = %{version}-%{release}
Requires:       python3-pillow-tk
Requires:       python3-tkinter

%description -n python3-matplotlib-tk
%{summary}

%if %{with wx}
%package -n     python3-matplotlib-wx
Summary:        WX backend for python3-matplotlib
BuildRequires:  python3dist(wxpython)
Requires:       python3-matplotlib%{?_isa} = %{version}-%{release}
Requires:       python3dist(wxpython)

%description -n python3-matplotlib-wx
%{summary}
%endif

%package -n python3-matplotlib-doc
Summary:        Documentation files for python-matplotlib
%if %{with html}
BuildRequires:  graphviz
BuildRequires:  make
BuildRequires:  python3dist(sphinx)
BuildRequires:  tex(latex)
BuildRequires:  tex-preview
%endif
Requires:       python3-matplotlib%{?_isa} = %{version}-%{release}

%description -n python3-matplotlib-doc
%{summary}

%package -n python3-matplotlib-test-data
Summary:        Test data for python3-matplotlib
Requires:       python3-matplotlib%{?_isa} = %{version}-%{release}

%description -n python3-matplotlib-test-data
%{summary}


%prep
%autosetup -n matplotlib-%{Version} -N

# Fedora-specific patches follow:
%autopatch -p1 -m 1000
# Updated test images for new FreeType.
gzip -dc %SOURCE1000 | tar xf - --transform='s~^mpl-images-%{mpl_images_version}-with-freetype-%{ftver}/~~'

# Copy mplsetup.cfg to the builddir
cp -p %{SOURCE1} mplsetup.cfg

# Backports or reported upstream
%autopatch -p1 -M 999
# https://github.com/matplotlib/matplotlib/pull/25068
cp -a %SOURCE2000 %SOURCE2001 lib/matplotlib/tests/baseline_images/test_backend_pgf/


%generate_buildrequires
%pyproject_buildrequires -r


%build
%set_build_flags
export http_proxy=http://127.0.0.1/

MPLCONFIGDIR=$PWD %pyproject_wheel
%if %{with html}
# Need to make built matplotlib libs available for the sphinx extensions:
MPLCONFIGDIR=$PWD \
PYTHONPATH="%{pyproject_site_lib}" \
    make -C doc html
%endif
# Ensure all example files are non-executable so that the -doc
# package doesn't drag in dependencies
find examples -name '*.py' -exec chmod a-x '{}' \;


%install
export http_proxy=http://127.0.0.1/

MPLCONFIGDIR=$PWD %pyproject_install

# Delete unnecessary files.
rm %{buildroot}%{python3_sitearch}/matplotlib/backends/web_backend/.{eslintrc.js,prettierignore,prettierrc}
rm %{buildroot}%{python3_sitearch}/matplotlib/tests/tinypages/.gitignore
rm %{buildroot}%{python3_sitearch}/matplotlib/tests/tinypages/_static/.gitignore

# Move files to Fedora-specific locations.
mkdir -p %{buildroot}%{_sysconfdir} %{buildroot}%{_datadir}/matplotlib
mv %{buildroot}%{python3_sitearch}/matplotlib/mpl-data \
   %{buildroot}%{_datadir}/matplotlib
%if %{without bundled_fonts}
rm -rf %{buildroot}%{_datadir}/matplotlib/mpl-data/fonts
%endif


%if %{with check}
%check
# These files confuse pytest, and we want to test the installed copy.
rm -rf build*/

# We need to prime this LaTeX cache stuff, or it might fail while running tests
# in parallel.
mktexfmt latex.fmt
mktexfmt lualatex.fmt
mktexfmt pdflatex.fmt
mktexfmt xelatex.fmt

export http_proxy=http://127.0.0.1/
# Skips:
#  * test_invisible_Line_rendering: Checks for "slowness" that often fails on a
#    heavily-loaded builder.
#  * test_form_widget_get_with_datetime_and_date_fields is flaky.
MPLCONFIGDIR=$PWD \
%ifnarch %{ix86}
     xvfb-run -a -s "-screen 0 640x480x24" \
%endif
         env %{pytest} -ra -n auto \
             -m 'not network' \
             -k 'not test_invisible_Line_rendering and not test_form_widget_get_with_datetime_and_date_fields' \
             --pyargs matplotlib mpl_toolkits.axes_grid1 mpl_toolkits.axisartist mpl_toolkits.mplot3d
%endif


%files -n python3-matplotlib-data
%{_datadir}/matplotlib/mpl-data/
%if %{with bundled_fonts}
%exclude %{_datadir}/matplotlib/mpl-data/fonts/
%endif

%if %{with bundled_fonts}
%files -n python3-matplotlib-data-fonts
%{_datadir}/matplotlib/mpl-data/fonts/
%endif

%files -n python3-matplotlib-doc
%doc examples
%if %{with html}
%doc doc/build/html/*
%endif

%files -n python3-matplotlib
%license LICENSE/
%doc README.md
%{python3_sitearch}/matplotlib-*.dist-info/
%{python3_sitearch}/matplotlib-*-nspkg.pth
%{python3_sitearch}/matplotlib/
%exclude %{python3_sitearch}/matplotlib/tests/baseline_images/*
%{python3_sitearch}/mpl_toolkits/
%exclude %{python3_sitearch}/mpl_toolkits/*/tests/baseline_images/*
%pycached %{python3_sitearch}/pylab.py
%pycached %exclude %{python3_sitearch}/matplotlib/backends/backend_qt5*.py
%pycached %exclude %{python3_sitearch}/matplotlib/backends/backend_gtk*.py
%pycached %exclude %{python3_sitearch}/matplotlib/backends/_backend_tk.py
%pycached %exclude %{python3_sitearch}/matplotlib/backends/backend_tk*.py
%exclude %{python3_sitearch}/matplotlib/backends/_tkagg.*
%pycached %exclude %{python3_sitearch}/matplotlib/backends/backend_wx*.py
%if %{with html}
%exclude %{_pkgdocdir}/*/
%endif

%files -n python3-matplotlib-test-data
%{python3_sitearch}/matplotlib/tests/baseline_images/
%{python3_sitearch}/mpl_toolkits/*/tests/baseline_images/

%files -n python3-matplotlib-qt5
%pycached %{python3_sitearch}/matplotlib/backends/backend_qt5*.py

# This is handled by backend_qt*.py (no number), so the package exists only for
# the dependencies.
%files -n python3-matplotlib-qt6

%files -n python3-matplotlib-gtk3
%pycached %{python3_sitearch}/matplotlib/backends/backend_gtk3*.py

%files -n python3-matplotlib-gtk4
%pycached %{python3_sitearch}/matplotlib/backends/backend_gtk4*.py

%files -n python3-matplotlib-tk
%pycached %{python3_sitearch}/matplotlib/backends/backend_tk*.py
%pycached %{python3_sitearch}/matplotlib/backends/_backend_tk.py
%{python3_sitearch}/matplotlib/backends/_tkagg.*

%if %{with wx}
%files -n python3-matplotlib-wx
%pycached %{python3_sitearch}/matplotlib/backends/backend_wx*.py
%endif


%changelog
%autochangelog
