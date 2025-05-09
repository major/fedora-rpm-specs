%global pypi_name torchvision

%bcond_with gitcommit
%if %{with gitcommit}
# The ToT
%global commit0 2c4665ffbb64f03f5d18016d3398af4ac4da5f03
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20240326 
%global pypi_version 0.19.0a0
%else
%global pypi_version 0.22.0
%endif

# check takes too long, make optional
%bcond_with test

# torch toolchain
%global toolchain gcc

Name:           python-%{pypi_name}
%if %{with gitcommit}
Version:        %{pypi_version}^git%{date0}.%{shortcommit0}
%else
Version:        %{pypi_version}
%endif
Release:        %autorelease
Summary:        Image and video datasets for torch deep learning

License:        BSD-3-Clause AND BSD-2-Clause AND MIT
URL:            https://github.com/pytorch/vision
%if %{with gitcommit}
Source0:        %{url}/archive/%{commit0}/vision-%{shortcommit0}.tar.gz
%else
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/vision-v%{version}.tar.gz
# https://github.com/pytorch/vision/pull/8096/commits/86620bd84b872b76db0acafec167949dca03a29e
#Patch1:         0001-AV_CODEC_CAP_INTRA_ONLY-is-not-defined.patch
%endif
# Need at least -g debugging
# Find where ffmpeg header and libs are
# Patch0:         0001-prepare-python-torchvision-setup-for-fedora.patch
Patch1:         0001-A-better-cuda-version.patch

# Limit to these because that is what torch is on
ExclusiveArch:  x86_64 aarch64

BuildRequires:  gcc-c++
BuildRequires:  ffmpeg-free
BuildRequires:  ffmpeg-free-devel
BuildRequires:  libavcodec-free-devel
BuildRequires:  libavformat-free-devel
BuildRequires:  libavutil-free-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  libswresample-free-devel
BuildRequires:  libswscale-free-devel
BuildRequires:  ninja-build
BuildRequires:  python3-devel
BuildRequires:  zlib-devel

BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(setuptools)

%if %{with test}
BuildRequires: python3dist(pytest)
%endif

Requires:      python3dist(numpy)
Requires:      python3dist(pillow)
Requires:      python3dist(requests)
Requires:      python3dist(torch)

%description
The torchvision package consists of popular datasets, model architectures,
and common image transformations for computer vision.

%package -n     python3-%{pypi_name}
Summary:        Image and video datasets for torch deep learning

%description -n python3-%{pypi_name}
The torchvision package consists of popular datasets, model architectures,
and common image transformations for computer vision.

%prep
%if %{with gitcommit}
%autosetup -p1 -n vision-%{commit0}
%else
%autosetup -p1 -n vision-%{version}
%endif

# Need some debug info
sed -i -e 's@extra_compile_args["cxx"].append("-g0")@extra_compile_args["cxx"].append("-g")@' setup.py
# Find ffmpeg on fedora
sed -i -e 's@ffmpeg_include_dir = os.path.join(ffmpeg_root, "include")@ffmpeg_include_dir = os.path.join(ffmpeg_root, "include/ffmpeg")@' setup.py
sed -i -e 's@ffmpeg_library_dir = os.path.join(ffmpeg_root, "lib")@ffmpeg_library_dir = os.path.join(ffmpeg_root, "lib64")@'              setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
# Building uses python3_sitearch/torch/utils/cpp_extension.py
# cpp_extension.py does a general linking with all the pytorch libs which
# leads warnings being reported by rpmlint.
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

# exec permission
for f in `find %{buildroot}%{python3_sitearch} -name '*.py'`; do
    if [ ! -x $f ]; then
        sed -i '1{\@^#!/usr/bin@d}' $f
    fi
done

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md 

# License details
# From license check output
#
# *No copyright* Creative Commons Attribution-NonCommercial 4.0
# -------------------------------------------------------------
# vision-0.16.0/README.md
# 
# - from this section of README.md
#
## Pre-trained Model License
#
# The pre-trained models provided in this library may have their own licenses or terms and conditions derived from the
# dataset used for training. It is your responsibility to determine whether you have permission to use the models for your
# use case.
# 

%changelog
%autochangelog
