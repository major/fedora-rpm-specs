%global pypi_name PySDL2

Name:           python-pysdl2
Version:        0.9.17
Release:        %{autorelease}
Summary:        Python SDL2 bindings

%global forgeurl https://github.com/py-sdl/py-sdl2
%global tag %{version}
%forgemeta

# For license approval and discussion see the mailing list
# https://lists.fedoraproject.org/archives/list/legal@lists.fedoraproject.org/thread/EHDGVB4HIBQ2N3UNHDGWQ654Q26OS766/#44KT5NKIT77ZWME464KDBYNH6WBCG4DA
License:        LicenseRef-Fedora-Public-Domain
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  SDL2
BuildRequires:  SDL2_gfx
BuildRequires:  SDL2_image
BuildRequires:  SDL2_mixer
BuildRequires:  SDL2_ttf
BuildRequires:  python3dist(pytest)

%global _description %{expand:
PySDL2 is a pure Python wrapper around the SDL2, SDL2_mixer,
SDL2_image, SDL2_ttf, and SDL2_gfx libraries. Instead of relying on C
code, it uses the built-in ctypes module to interface with SDL2, and
provides simple Python classes and wrappers for common SDL2
functionality.}

%description %_description


%package -n python3-pysdl2
Summary:        %{summary}
Requires:       SDL2
Requires:       SDL2_gfx
Requires:       SDL2_image
Requires:       SDL2_mixer
Requires:       SDL2_ttf

%description -n python3-pysdl2 %_description


%prep
%forgeautosetup -p1

# Make sure we actually ship the file containing the license
# `COPYING.txt` only contains one line: See doc/copying.rst
rm -vf COPYING.txt
mv -v doc/copying.rst COPYING.rst

# Don't ship examples and test
sed -r \
    -e '/sdl2\.examples/ d' \
    -e '/sdl2\.test/ d' \
    -i setup.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l sdl2


%check
# Set up environment
# https://github.com/py-sdl/py-sdl2/blob/master/.github/workflows/run_tests.yml
export SDL_VIDEODRIVER=dummy
export SDL_AUDIODRIVER=dummy
export SDL_RENDER_DRIVER=software
export PYTHONFAULTHANDLER=1

# Skip game controller tests (no dummy device implemented)
%pytest -v --ignore sdl2/test/gamecontroller_test.py


%files -n python3-pysdl2 -f %{pyproject_files}
%doc README.md AUTHORS.txt


%changelog
%autochangelog
