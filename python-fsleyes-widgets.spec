# These are unreliable, unfortunately.
%bcond_with xvfb_tests

%global desc \
A collection of custom wx widgets and utilities used by FSLeyes.


Name:           python-fsleyes-widgets
Version:        0.13.0
Release:        %autorelease
Summary:        A collection of custom wx widgets and utilities used by FSLeyes

License:        Apache-2.0
URL:            https://pypi.python.org/pypi/fsleyes-widgets
Source0:        %{pypi_source fsleyes-widgets}

BuildArch:      noarch
BuildRequires:  python3-devel
%if %{with xvfb_tests}
BuildRequires:  xorg-x11-server-Xvfb
%endif

%description
%{desc}

%package -n python3-fsleyes-widgets
Summary:        %{summary}

%description -n python3-fsleyes-widgets
%{desc}

# do not generate docs because sphinx docs bundle js etc. which are very hard to unbundle

%prep
%autosetup -n fsleyes-widgets-%{version}

# remove unneeded shebangs
find . -name "*py" -exec sed -i '/#!\/usr\/bin\/env python/ d' '{}' \;

# remove sphinx from requirements because we're not generating sphinx docs
sed -i '/sphinx/ d' requirements-dev.txt

%generate_buildrequires
%pyproject_buildrequires -r requirements-dev.txt requirements.txt


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files fsleyes_widgets


%check
%if %{with xvfb_tests}
# From https://git.fmrib.ox.ac.uk/fsl/fsleyes/widgets/blob/master/.ci/test_template.sh
# These tests fail, so Ive disabled them for the time being. Upstream has been e-mailed.
# set sceen size for test_widgetgrid.py
# cannot use %%pytest, xvfb doesnt like the CFLAGS etc. that it sets
xvfb-run -a -s "-screen 0 1920x1200x24" pytest-3 tests --ignore=tests/test_autotextctrl.py --ignore=tests/test_bitmapradio.py --ignore=tests/test_bitmaptoggle.py --ignore=tests/test_colourbutton.py --ignore=tests/test_floatslider.py --ignore=tests/test_notebook.py --ignore=tests/test_rangeslider.py --ignore=tests/test_texttag.py --ignore=tests/test_numberdialog.py
%endif

%files -n python3-fsleyes-widgets -f %{pyproject_files}
%license LICENSE COPYRIGHT
%doc README.rst

%changelog
%autochangelog
