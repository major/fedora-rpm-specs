# Upstream doesn’t (so far) push git tags for releases, but does keep a version
# number for the library. Since this commit certainly corresponds precisely to
# the packaged version, we don’t use a snapshot info field in the Version.
%global commit 2768987dbd7119eb840104b7a3f96ff09d21a7b4

Name:           stb_image_resize
Version:        2.50
Release:        %autorelease
Summary:        Image resizing

License:        MIT OR Unlicense
URL:            https://github.com/nothings/stb_image_resize
Source:         %{url}/archive/%{commit}/stb_image_resize-%{commit}.tar.gz

# Add a dedicated LICENSE file
# https://github.com/nothings/stb_image_resize/pull/1
#
# We consider this OK to do downstream because the license text exactly matches
# what is already in the source file.
Patch:          %{url}/pull/1.patch

BuildRequires:  gcc

# This is a header-only library with no compiled binaries.
%global debug_package %{nil}

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%package -n stb_image_resize2-devel
Summary:        %{summary}

BuildArch:      noarch

Provides:       stb_image_resize2-static = %{version}

%description -n stb_image_resize2-devel %{common_description}


%prep
%autosetup -n stb_image_resize-%{commit} -p1


# Header-only library; nothing to build


%install
# Since this is designed to be copied into dependent package source trees,
# there is no convention on include path. Considering the other stb libraries,
# most projects end up using “#include <stb_foo.h>” or “#include
# <stb/stb_foo.h>”, so we install to %%{_includedir}/stb/stb_foo.h and
# %%{_includedir}/stb_foo.h, with the latter as a symbolic link to the former.
# This means most projects can unbundle the library without having to make
# their own local symlinks or patch their sources.
install -D --preserve-timestamps --mode=0644 \
    --target='%{buildroot}%{_includedir}/stb' stb_*.h
pushd '%{buildroot}%{_includedir}'
ln --symbolic --verbose stb/stb_*.h .
popd


%check
# This is only needed (explicitly) in EPEL8/9:
%set_build_flags

# There is nothing in stb_image_resize_test/ that is suitable to use here; the
# contents of that directory are more like development and analysis tooling.
# Let’s at least make sure that the library can be compiled.
cat > smoke_test.c <<'EOF'
#include "stb_image_resize2.h"
#define STB_IMAGE_RESIZE_IMPLEMENTATION
int main(int argc, char *argv[]) { return 0; }
EOF
${CC-gcc} -c smoke_test.c -o smoke_test.o ${CFLAGS} -I.
${CC-gcc} -o smoke_test smoke_test.o ${LDFLAGS}
# No need to run the executable; building it was the test.


%files -n stb_image_resize2-devel
%license LICENSE
# Directory has shared ownership across stb libraries:
%dir %{_includedir}/stb
%{_includedir}/stb/stb_image_resize2.h
%{_includedir}/stb_image_resize2.h


%changelog
%autochangelog
