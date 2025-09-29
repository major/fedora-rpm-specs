%global         srcname  img2pdf
%global         desc   Python 3 library and command line utility img2pdf for losslessly converting\
a bunch of image files into a PDF file. That means that the images\
are either inserted into the PDF as-is or they are recompressed using\
lossless compression. Thus, img2pdf usually runs faster and may yield\
smaller PDF files than an ImageMagick convert command.\
\
The img2pdf command complements the pdfimages command.

Name:           python-%{srcname}
Version:        0.6.1
Release:        %autorelease
Summary:        Lossless images to PDF conversion library and command

License:        LGPL-3.0-or-later
URL:            https://pypi.org/project/img2pdf
Source0:        %pypi_source

# XXX remove when https://gitlab.mister-muffin.de/josch/img2pdf/issues/204 is fixed
Patch0:         magick-prog.patch
# XXX remove when https://gitlab.mister-muffin.de/josch/img2pdf/pulls/211 is resolved
Patch1:         add-tox-ini.diff


BuildArch:      noarch

# Disable tests on EPEL8 for now, since some of the dependencies aren't available
%if 0%{?epel} == 0
# required for tests
BuildRequires:  ImageMagick
BuildRequires:  ghostscript
BuildRequires:  libtiff-tools
BuildRequires:  mupdf
BuildRequires:  netpbm-progs
BuildRequires:  perl-Image-ExifTool
BuildRequires:  poppler-utils
BuildRequires:  icc-profiles-openicc
%endif

# other requirements
BuildRequires:  python3-devel

# The Python dependency generator is enabled by default since f30 or so.
# It adds `Requires:` for:
#
# pikepdf
# pillow


%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}

%prep
%autosetup -p1 -n %{srcname}-%{version}

# disable in EPEL builds since pikepdf isn't available on CentOS 8/EPEL
# (img2pdf then falls back to its internal PDF engine)
#
# alternatively, we could disable the python dependency generator, however as of 2020-12
# the necessary disable macro isn't available in the epel8 build environment
# cf. https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/SI5CXXV3MWMEH3PLKAVAJK22FRNI7OGM/
%if 0%{?epel} != 0
sed -i '/^INSTALL_REQUIRES/,/)/s/\("pikepdf".*$\)/### not available on EPEL ### \1/' setup.py
%endif


%generate_buildrequires
%pyproject_buildrequires -t


%build
sed -i '1{/^#!\//d}' src/*.py
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{srcname} jp2


%check

%if 0%{?epel} == 0

# since the test directly calls src/img2pdf.py
# (file is already installed at this point)
sed -i '1i#!'%{__python3} src/img2pdf.py

# cf. https://gitlab.mister-muffin.de/josch/img2pdf/issues/178
#     https://gitlab.mister-muffin.de/josch/img2pdf/issues/187
#     https://gitlab.mister-muffin.de/josch/img2pdf/issues/210
# XXX TODO enable again after issue is resolved
PYTHONPATH=src %{__python3} -m pytest src/img2pdf_test.py -v -k 'not miff_c and not png_icc and not png_rgb16 and not png_gray16'

%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%{_bindir}/%{srcname}
%{_bindir}/%{srcname}-gui
%doc README.md CHANGES.rst


%changelog
%autochangelog
