#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : phonon-vlc
Version  : 0.10.2
Release  : 1
URL      : https://github.com/KDE/phonon-vlc/archive/v0.10.2.tar.gz
Source0  : https://github.com/KDE/phonon-vlc/archive/v0.10.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause LGPL-2.1
Requires: phonon-vlc-lib = %{version}-%{release}
Requires: phonon-vlc-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : phonon-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libvlc)
BuildRequires : vlc-dev

%description
No detailed description available

%package lib
Summary: lib components for the phonon-vlc package.
Group: Libraries
Requires: phonon-vlc-license = %{version}-%{release}

%description lib
lib components for the phonon-vlc package.


%package license
Summary: license components for the phonon-vlc package.
Group: Default

%description license
license components for the phonon-vlc package.


%prep
%setup -q -n phonon-vlc-0.10.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1559860837
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake .. -DPHONON_BUILD_PHONON4QT5=ON
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1559860837
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/phonon-vlc
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/phonon-vlc/COPYING.LIB
cp cmake/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/phonon-vlc/cmake_COPYING-CMAKE-SCRIPTS
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/phonon4qt5_backend/phonon_vlc.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/phonon-vlc/COPYING.LIB
/usr/share/package-licenses/phonon-vlc/cmake_COPYING-CMAKE-SCRIPTS
