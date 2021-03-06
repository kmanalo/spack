# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Xtrap(AutotoolsPackage):
    """XTrap sample clients."""

    homepage = "http://cgit.freedesktop.org/xorg/app/xtrap"
    url      = "https://www.x.org/archive/individual/app/xtrap-1.0.2.tar.gz"

    version('1.0.2', sha256='e8916e05bfb0d72a088aaaac0feaf4ad7671d0f509d1037fb3c0c9ea131b93d2')

    depends_on('libx11')
    depends_on('libxtrap')

    depends_on('pkgconfig', type='build')
    depends_on('util-macros', type='build')
